from ctypes import *
import CANapAPI
import time
import pysnooper

dll_version_t = CANapAPI.version_t(0,0,0,b"null",0) 
ret = CANapAPI.Asap3GetVersion(byref(dll_version_t))
print(dll_version_t.osVersion)
print(ret)

Hdl = CANapAPI.TAsap3Hdl()  # c <=> TAsap3Hdl Hdl = NULL;

@pysnooper.snoop(depth=3)
def startCA():
    responseTimeout = c_uint32(200000)
    workingDir = c_char_p(b"C:\\Users\\Public\\Documents\\Vector CANape 19.0\\ExampleDAQXCPSys")
    fifoSize = c_uint32(8000)
    sampleSize = c_uint32(320)
    debugMode = c_bool(True)
    clearDeviceList = c_bool(False)
    bHexmode = c_bool(False)
    bModalMode = c_bool(True)

    # dont know why 'Hdl' gets converted into PointerPointer, probably by argtypes of fcn
    ret = CANapAPI.Asap3Init5(Hdl, responseTimeout, workingDir, fifoSize, sampleSize, debugMode, clearDeviceList, bHexmode, bModalMode)
    return ret


startCA()

time.sleep(2)

CANapAPI.Asap3PopupDebugWindow(Hdl)

time.sleep(2)


# extern bool ASAP3_EXPORT CALL_CONV Asap3SetInteractiveMode(TAsap3Hdl hdl,bool mode);
# ret = CANapAPI.Asap3SetInteractiveMode(Hdl, c_bool(True))


# Pass in TAsap3Hdl Instance (aka tAsap3Hdl pointer) to Asap3Exit
print(f"Exiting CANape (Handle: {Hdl}) ...")
ret = CANapAPI.Asap3Exit(Hdl)
print(f"... done (ret: {ret})")