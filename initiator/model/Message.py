from model import Field
# import FIX42

class Types(object):
    Logon = 'A'
    Heartbeat = '0'
    TestRequest = '1'
    Logout = '5'
    ResendRequest = '2'
    Reject = '3'
    SequenceReset = '4'
    MarketDataRequest = 'V'
    MarketDataSnapshot = 'W'
    MarketDataRefresh = 'X'
    NewOrder = 'D'
    ListOrder = 'E'
    OrderCancel = 'F'
    OrderCancelReplace = 'G'
    DontKnowTrade = 'Q'
    OrderStatus = 'H'
    ExecutionReport = '8'
    OrderCancelReject = '9'
    BusinessMessageReject = 'j'
    PositionRequest = 'AN'
    PositionReport = 'AP'

__SOH__ = chr(1)

def build_checksum(message):
    checksum = sum([ord(i) for i in list(message)]) % 256
    return make_pair((10, str(checksum).zfill(3)))


def make_pair(pair):
    return str(pair[0]) + "=" + str(pair[1]) + __SOH__

class Base(object):
    default_session = None
    current_session = None
    # msg_type = None
    # fields = []
    # length = None
    # string = None

    def __init__(self, fields=None, session=None):
        self.msg_type = None
        self.fields = []

        if fields is None:
            fields = []

        for pair in fields:
            self.set_field(pair)

        self.length = None
        self.string = None

        # if not session and not self.default_session:
        #     raise RuntimeError('Session must be provided if default session is not set')

        if not session:
            self.current_session = self.default_session
        else:
            self.current_session = session

    def __getitem__(self, item):
        return self.get_field(item)

    def __setitem__(self, key, value):
        return self.set_field((key, value))

    def toString(self):
        return self.string.replace(__SOH__, "|")

    def get_type(self):
        return self.msg_type

    def get_field(self, field_type):
        for pair in self.fields:
            if str(pair[0]) == str(field_type):
                return pair[1]
        return None

    def set_field(self, pair):
        if str(pair[0]) == str(Field.MsgType):
            self.msg_type = pair[1]

        self.fields.append(pair)
        # self.length = None
        # self.string = None
        return self

    def get_all_by(self, field_type):
        result = []
        for pair in self.fields:
            if str(pair[0]) == str(field_type):
                result.append(pair[1])
        return result

    def get_group(self, group):
        result = []
        for field_id in group:
            values = self.get_all_by(field_id)
            for i, value in enumerate(values):
                if len(result) - 1 < i:
                    result.append({})
                result[i][field_id] = value
        return result
    
    def parse_string(self, string, session):
        result = Base(None, session)
        for pair in string.split(__SOH__):
            if len(pair):
                values = pair.split('=')
                if len(values) == 2:
                    result.set_field((values[0], values[1]))
        result.string = string
        return result


class SanGiaoDich:
    HOSE = '01'
    HNX = '03'
    UPCOM = '05'

class ErrorCodeIs:
    Reject = '0000'
    NotSupportOrdType = '0001'
    NotSupportTimeInForce= '0002'
    SymbolNotExist = '0003'
    TimeInForce_DAY = 'DAY'
    TimeInForce_GTC = 'GTC'
    TimeInForce_OPG = 'OPG'
    TimeInForce_IOC = 'IOC'
    TimeInForce_FOK = 'FOK'
    TimeInForce_GTX = 'GTX'
    TimeInForce_GTD = 'GTD'

class TimeInForceIs:
    DAY = '0'
    GTC = '1' # Good Till Cancel 
    OPG = '2' # At the Opening
    IOC = '3' # Immediate or Cance
    FOK = '4' # Fill or Kill
    GTX = '5' # Good Till Crossing
    GTD = '6' # Good Till Date

class OrdTypeALT:
    LO = '01'
    MP = '02'
    ATO = '03'
    ATC = '04'
    MOK = '06'
    MAK = '07'
    MTL = '08'

    @staticmethod
    def getOrdType(code=None, SanGD=None, atc=False):
        if SanGD == SanGiaoDich.HNX:
            if atc == True: # Phien cuoi ngay
                return OrdTypeALT.ATC
            if code == TimeInForceIs.DAY: # Phien lien tuc
                return OrdTypeALT.MAK
            if code == TimeInForceIs.FOK: # Khop het hoac Canceled
                return OrdTypeALT.MOK
            if code == TimeInForceIs.IOC: # Khop het, khop mot phan hoac Canceled phan con lai
                return OrdTypeALT.MAK
            if code == TimeInForceIs.OPG:
                return OrdTypeALT.ATC
            if code == None:
                return OrdTypeALT.MAK
            return None
        elif SanGD == SanGiaoDich.HOSE:
            if atc == True:
                return OrdTypeALT.ATC # Phien cuoi ngay
            if code == TimeInForceIs.OPG:
                return OrdTypeALT.ATC # Phien dau ngay
            return None
        elif SanGD == SanGiaoDich.UPCOM:
            return None

class OrdTypeBLP:
    Market = '1'
    Limit = '2'
    MarketOnClose = '5'
    LimitOnClose = 'B'

