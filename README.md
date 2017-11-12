# passnrcheck

simple script to calculate checkdigits for (EU) passport numbers. 
could in theory be used for age verification systems that need a passport serialnumber + birthdate(+checkdigit) to check your age.
for educational purposes only.

see also:
  * https://pinetik.blogspot.co.at/2011/03/prufziffer-fur-neuen-reisepass.html
  * https://www.icao.int/Security/mrtd/Downloads/Doc%209303/Doc%209303%20English/Doc%209303%20Part%201%20Vol%201.pdf#search=Doc%209303%20Part%201%20Vol%201
     * (page 65 in the pdf, "check digits in the machine readable zone")

## passport number format:
```
sernum checkdigit(sernum)              NationIdentifier        birthdate (inverse/yymmdd) checkdigit(birthdate)        gender(m/f)     expirationdate (invers/yymmdd)  checkdigit(expirationdate) <<...<< checkdigit(overall)
```
