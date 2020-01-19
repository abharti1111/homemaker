from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validatePhoneNumber(number):
    if len(str(number))!=10 :
        raise ValidationError(
            _('%(number)s is not a valid phone number'),
            params={'number':number}
        )
def ValidatePanId(panId):
    if not (panId[:5].isalpha() and panId[:5].isupper() and (not panId[5:9].isalpha()) and panId[-1].isalpha()):
        raise ValidationError(
        _('%(panId)s is not a valid Pan Number'),
        params={'panId':panId}
    )

def ValidatePinCode(pinCode):
    if len(str(pinCode))!=6:
        raise ValidationError(
        _('%(pinCode)s is not a valid pin Code'),
        params={'panId':panId}
    )
