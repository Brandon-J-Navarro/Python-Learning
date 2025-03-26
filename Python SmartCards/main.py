# pip3 install chilkat
import sys
import chilkat

def find_smart_cards():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scard = chilkat.CkSCard()

    # First establish a context to the PC/SC Resource Manager
    success = scard.EstablishContext("user")
    if (success == False):
        print(scard.lastErrorText())
        sys.exit()

    # Get JSON containing information about the smartcards currently inserted into readers.
    # This also includes information about USB security tokens.
    json = chilkat.CkJsonObject()
    success = scard.FindSmartcards(json)
    if (success == False):
        print(scard.lastErrorText())
        sys.exit()

    json.put_EmitCompact(False)
    print(json.emit())

def list_readers():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scard = chilkat.CkSCard()

    # First establish a context to the PC/SC Resource Manager
    success = scard.EstablishContext("user")
    if (success == False):
        print(scard.lastErrorText())
        sys.exit()

    stReaders = chilkat.CkStringTable()
    success = scard.ListReaders(stReaders)
    if (success == False):
        print(scard.lastErrorText())
        sys.exit()

    numReaders = stReaders.get_Count()
    i = 0
    while i < numReaders:
        print(str(i) + ": " + stReaders.stringAt(i))
        i = i + 1

    # Sample output:
    # 0: Alcor Micro USB Smart Card Reader 0
    # 1: FS USB Token 0
    # 2: FT Java Token 0
    # 3: SCM Microsystems Inc. SCR33x USB Smart Card Reader 0
    # 4: Yubico YubiKey OTP+FIDO+CCID 0

    # Applications should always release the context when finished.
    success = scard.ReleaseContext()
    if (success == False):
        print(scard.lastErrorText())

def list_certificates():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scmd = chilkat.CkScMinidriver()

    # Reader names (smart card readers or USB tokens) can be discovered
    # via PCSC List Readers or PCSC Find Smart Cards
    readerName = "SCM Microsystems Inc. SCR33x USB Smart Card Reader 0"
    success = scmd.AcquireContext(readerName)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    stCerts = chilkat.CkStringTable()

    # We can choose one of the following items of information to get for each certificate:
    # "subjectDN" -- Return the full distinguished name of the cert.
    # "subjectDN_withTags" -- Same as above, but in a format that includes the subject part tags, such as the "CN=" in "CN=something"
    # "subjectCN" -- Return just the common name part of the certificate's subject.
    # "serial" -- Return the certificate serial number.
    # "serial:issuerCN" -- return the certificate serial number + the issuer's common name, delimited with a colon char.
    certPart = "subjectCN"

    success = scmd.ListCerts(certPart, stCerts)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    numCerts = stCerts.get_Count()
    i = 0
    while i < numCerts:
        print(str(i) + ": " + stCerts.stringAt(i))
        i = i + 1

    # Delete the context when finished with the card.
    success = scmd.DeleteContext()
    if (success == False):
        print(scmd.lastErrorText())

def get_smartcard_properties():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scmd = chilkat.CkScMinidriver()

    # Reader names (smart card readers or USB tokens) can be discovered
    # via PCSC List Readers or PCSC Find Smart Cards
    readerName = "SCM Microsystems Inc. SCR33x USB Smart Card Reader 0"
    success = scmd.AcquireContext(readerName)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    json = chilkat.CkJsonObject()
    json.put_EmitCompact(False)

    success = scmd.GetCardProperties(json)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    print(json.emit())

def auth_example():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scmd = chilkat.CkScMinidriver()

    # Reader names (smart card readers or USB tokens) can be discovered
    # via List Readers or Find Smart Cards
    readerName = "SCM Microsystems Inc. SCR33x USB Smart Card Reader 0"
    success = scmd.AcquireContext(readerName)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    # If we are successful, the name of the currently inserted smart card is available:
    cardName = scmd.cardName()
    print("Card name: " + cardName)

    # Perform regular PIN authentication with the smartcard.
    # If authentication is successful, then the ScMinidriver session is authenticated and
    # operations such as signing are permissible.

    # The pin ID can be "user", "admin", or a number "3" through "7" (passed as a string).
    # The possible pin ID's for a given smartcard are obtained via the GetCardProperties method.
    # See Get Smart Card Properties for sample code.
    # You should generally use the "user" pin ID.  You would only use the other pin ID's for very specific purposes.
    pinId = "user"

    # Change this to the PIN for your smart card.
    pin = "0000000"

    retval = scmd.PinAuthenticate(pinId, pin)

    # The return value is 0 for success.
    # If the retval is greater than 0, it is the number of attempts remaining before the PIN is blocked.
    # If the retval equals -1, then something else went wrong and you should consult the LastErrorText.
    if (retval < 0):
        print(scmd.lastErrorText())
        sys.exit()

    if (retval > 0):
        print("PIN authentcation failed, " + str(retval) + " attempts remaining before the PIN is blocked.")
    else:
        print(
            "PIN authentication successful. Your session is now authenticated and you may proceed with operations such as signing.")

    # ...
    # ...
    # ...

    # You may deauthenticate the session when finished with operations that required authentication.
    success = scmd.PinDeauthenticate(pinId)
    if (success == False):
        print(scmd.lastErrorText())

    # Delete the context when finished with the card.
    success = scmd.DeleteContext()
    if (success == False):
        print(scmd.lastErrorText())


def example():
    # This example requires the Chilkat API to have been previously unlocked.
    # See Global Unlock Sample for sample code.

    scmd = chilkat.CkScMinidriver()

    # Reader names (smart card readers or USB tokens) can be discovered
    # via List Readers or Find Smart Cards
    readerName = "SCM Microsystems Inc. SCR33x USB Smart Card Reader 0"
    success = scmd.AcquireContext(readerName)
    if (success == False):
        print(scmd.lastErrorText())
        sys.exit()

    # If successful, the name of the currently inserted smart card is available:
    print("Card name: " + scmd.cardName())

    # If desired, perform regular PIN authentication with the smartcard.
    # For more details about smart card PIN authentication, see the Smart Card PIN Authentication Example
    retval = scmd.PinAuthenticate("user", "0000000")
    if (retval != 0):
        print("PIN Authentication failed.")

    # You can find a cerficate using any of the following certificate parts:
    # "subjectDN" -- The full distinguished name of the cert.
    # "subjectDN_withTags" -- Same as above, but in a format that includes the subject part tags, such as the "CN=" in "CN=something"
    # "subjectCN" -- The common name part (CN) of the certificate's subject.
    # "serial" -- The certificate serial number.
    # "serial:issuerCN" -- The certificate serial number + the issuer's common name, delimited with a colon char.
    # These are the same certificate parts that can be retrieved by listing certificates on the smart card (or USB token).
    # See List Certificates on Smart Card Example
    certPart = "serial"
    partValue = "000000"

    # If the certificate is found, it is loaded into the cert object.
    # Note: We imported this certificate from a .p12/.pfx using this Example to Import a .pfx/.p12 onto a Smart Card
    cert = chilkat.CkCert()
    success = scmd.FindCert(certPart, partValue, cert)
    if (success == False):
        print("Failed to find the certificate.")
        scmd.DeleteContext()
        sys.exit()

    print("Successfully loaded the cert object from the smart card / USB token.")

    # Note: When successful, the cert object is internally linked to the ScMinidriver object's authenticated session.
    # The cert object can now be used to sign or do other cryptographic operations that occur on the smart card / USB token.
    # If your application calls PinDeauthenticate or DeleteContext, the cert will no longer be able to sign on the smart card
    # because the smart card ScMinidriver session will no longer be authenticated or deleted.

    # ------------------------------------------------------------------------------------------------------------

    # Send an HTTPS request to https://client.badssl.com
    # https://client.badssl.com (part of the badssl.com service) lets you test authentication using client SSL certificates.
    # The client certificate can be downloaded from https://badssl.com/download/.
    # This server returns 200 OK if the correct client certificate is provided, and 400 Bad Request otherwise.

    http = chilkat.CkHttp()

    # Provide the client certificate (linked internally to our authenticated smartcard session)
    success = http.SetSslClientCert(cert)
    if (success == False):
        print(http.lastErrorText())
        scmd.DeleteContext()
        sys.exit()

    http.SetRequestHeader('Content-type', 'application/json')

    responseBody = http.QuickRequest("POST","https://domain.com/")
    if (http.get_LastMethodSuccess() == False):
        print(http.lastErrorText())
        scmd.DeleteContext()
        sys.exit()

    print("Response status code: " + str(http.get_LastStatus()))
    print("Response body: ")
    print(responseBody)

    # ------------------------------------------------------------------------------------------------------------
    # Cleanup our ScMinidriver session...

    # When finished with operations that required authentication, you may if you wish, deauthenticate the session.
    success = scmd.PinDeauthenticate("user")
    if (success == False):
        print(scmd.lastErrorText())

    # Delete the context when finished with the card.
    success = scmd.DeleteContext()
    if (success == False):
        print(scmd.lastErrorText())


if __name__ == '__main__':
    # find_smart_cards()
    # list_readers()
    # get_smartcard_properties()
    # list_certificates()
    # auth_example()
    example()