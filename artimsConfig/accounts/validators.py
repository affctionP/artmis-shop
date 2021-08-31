from django.core.exceptions import ValidationError
from django.core.validators  import RegexValidator
reg_mob=r'^09(1[0-9]|3[1-9]|2[1-9]|0[1-9])-?[0-9]{3}-?[0-9]{4}$'
reg_home = r'^0[0-9]{2,}[0-9]{7,}$'

PHONE_NUMBER_REGEX = RegexValidator(reg_mob, 'only valid mobile phone  is required')





