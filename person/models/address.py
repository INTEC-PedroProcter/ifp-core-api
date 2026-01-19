import uuid
from django.db import models
from django.contrib.auth import get_user_model
from person.models.person import Person


COUNTRY_CODES_ISO2 = (
    "AF","AL","DZ","AS","AD","AO","AI","AQ","AG","AR","AM","AW","AU","AT","AZ",
    "BS","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BQ","BA","BW","BR",
    "IO","BN","BG","BF","BI","KH","CM","CA","CV","KY","CF","TD","CL","CN","CX",
    "CC","CO","KM","CG","CD","CK","CR","CI","HR","CU","CW","CY","CZ","DK","DJ",
    "DM","DO","EC","EG","SV","GQ","ER","EE","ET","FK","FO","FJ","FI","FR","GF",
    "PF","TF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GU","GT","GG",
    "GN","GW","GY","HT","HM","VA","HN","HK","HU","IS","IN","ID","IR","IQ","IE",
    "IM","IL","IT","JM","JP","JE","JO","KZ","KE","KI","KP","KR","KW","KG","LA",
    "LV","LB","LS","LR","LY","LI","LT","LU","MO","MG","MW","MY","MV","ML","MT",
    "MH","MQ","MR","MU","YT","MX","FM","MD","MC","MN","ME","MS","MA","MZ","MM",
    "NA","NR","NP","NL","NC","NZ","NI","NE","NG","NU","NF","MK","MP","NO","OM",
    "PK","PW","PS","PA","PG","PY","PE","PH","PN","PL","PT","PR","QA","RE","RO",
    "RU","RW","BL","SH","KN","LC","MF","PM","VC","WS","SM","ST","SA","SN","RS",
    "SC","SL","SG","SX","SK","SI","SB","SO","ZA","GS","SS","ES","LK","SD","SR",
    "SJ","SZ","SE","CH","SY","TW","TJ","TZ","TH","TL","TG","TK","TO","TT","TN",
    "TR","TM","TC","TV","UG","UA","AE","GB","US","UM","UY","UZ","VU","VE","VN",
    "VG","VI","WF","EH","YE","ZM","ZW"
)
INVALID_COUNTRY_CODE_MESSAGE = "Country code must be in ALPHA2 format."

class PersonAddress(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.TextField(max_length=128, blank=False)
    township = models.TextField(max_length=128, blank=False)
    city = models.TextField(max_length=128, blank=False)
    province = models.TextField(max_length=128, blank=False)
    country_code = models.TextField(max_length=2, blank=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "PersonAddress"
        managed = False
        constraints = [
            models.CheckConstraint(
                condition=models.Q(country_code__in=COUNTRY_CODES_ISO2),
                name="CK_PersonAddress_Country_Code_ISO2",
                violation_error_message="Country code must be in ALPHA2 format."
            )
        ]

    def __str__(self):
        return f'{self.street}, {self.city}, {self.township}, {self.province}, {self.country_code} ({self.person.national_id})'