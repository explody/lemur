from lemur.common.utils import parse_certificate

VALID_USER_HEADER_TOKEN = {
    'Authorization': 'Basic ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MjE2NTIwMjIsImV4cCI6MjM4NTY1MjAyMiwic3ViIjoxfQ.uK4PZjVAs0gt6_9h2EkYkKd64nFXdOq-rHsJZzeQicc',
    'Content-Type': 'application/json'
}


VALID_ADMIN_HEADER_TOKEN = {
    'Authorization': 'Basic ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjE2NTE2NjMsInN1YiI6MiwiYWlkIjoxfQ.wyf5PkQNcggLrMFqxDfzjY-GWPw_XsuWvU2GmQaC5sg',
    'Content-Type': 'application/json'
}


VALID_ADMIN_API_TOKEN = {
    'Authorization': 'Basic ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjIsImFpZCI6MSwiaWF0IjoxNDM1MjMzMzY5fQ.umW0I_oh4MVZ2qrClzj9SfYnQl6cd0HGzh9EwkDW60I',
    'Content-Type': 'application/json'
}

DEFAULT_SANS = ['san.example.org', 'san2.example.org', 'daniel-san.example.org']

#: CN=LemurTrust Unittests Root CA 2018
ROOTCA_CERT_STR = """\
-----BEGIN CERTIFICATE-----
MIIEFjCCAv6gAwIBAgIQbIbX/Ap0Roqzf5HeN5akmzANBgkqhkiG9w0BAQsFADCB
pDEqMCgGA1UEAwwhTGVtdXJUcnVzdCBVbml0dGVzdHMgUm9vdCBDQSAyMDE4MSMw
IQYDVQQKDBpMZW11clRydXN0IEVudGVycHJpc2VzIEx0ZDEmMCQGA1UECwwdVW5p
dHRlc3RpbmcgT3BlcmF0aW9ucyBDZW50ZXIxCzAJBgNVBAYTAkVFMQwwCgYDVQQI
DANOL0ExDjAMBgNVBAcMBUVhcnRoMB4XDTE3MTIzMTIyMDAwMFoXDTQ3MTIzMTIy
MDAwMFowgaQxKjAoBgNVBAMMIUxlbXVyVHJ1c3QgVW5pdHRlc3RzIFJvb3QgQ0Eg
MjAxODEjMCEGA1UECgwaTGVtdXJUcnVzdCBFbnRlcnByaXNlcyBMdGQxJjAkBgNV
BAsMHVVuaXR0ZXN0aW5nIE9wZXJhdGlvbnMgQ2VudGVyMQswCQYDVQQGEwJFRTEM
MAoGA1UECAwDTi9BMQ4wDAYDVQQHDAVFYXJ0aDCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAL8laXtLXyM64t5dz2B9q+4VvOsChefBi2PlGudqxDuRN3l0
Kmcfun6x2Gng24pTlGdtmiTEWA0a2F8HRLv4YBWhuYleVeBPtf1fF1/SuYgkJOWT
7S5qk/od/tUOLHS0Y067st3FydnFQTKpAuYveEkxleFrMS8hX8cuEgbER+8ybiXK
n4GsyM/om6lsTyBoaLp5yTAoQb4jAWDbiz1xcjPSkvH2lm7rLGtKoylCYwxRsMh2
nZcRr1OXVhYHXwpYHVB/jVAjy7PAWQ316hi6mpPYbBV+yfn2GUfGuytqyoXLEsrM
3iEEAkU0mJjQmYsCDM3r7ONHTM+UFEk47HCZJccCAwEAAaNCMEAwDwYDVR0TAQH/
BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFFL12SFeOTTDdGKsHKoz
eByGHY6nMA0GCSqGSIb3DQEBCwUAA4IBAQAJfe0/uAHobkxth38dqrSFmTo+D5/T
MlRt3hdgjlah6sD2+/DObCyut/XhQWCgTNWyRi4xTKgLh5KSoeJ9EMkADGEgDkU2
vjBg5FmGZsxg6bqjxehK+2HvASJoTH8r41xmTioav7a2i3wNhaNSntw2QRTQBQED
OIzHRpPDQ2quErjA8nSifE2xmAAr3g+FuookTTJuv37s2cS59zRYsg+WC3+TtPpR
ssvobJ6Xe2D4cCVjUmsqtFEztMgdqgmlcWyGdUKeXdi7CMoeTb4uO+9qRQq46wYW
n7K1z+W0Kp5yhnnPAoOioAP4vjASDx3z3RnLaZvMmcO7YdCIwhE5oGV0
-----END CERTIFICATE-----
"""
ROOTCA_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAvyVpe0tfIzri3l3PYH2r7hW86wKF58GLY+Ua52rEO5E3eXQq
Zx+6frHYaeDbilOUZ22aJMRYDRrYXwdEu/hgFaG5iV5V4E+1/V8XX9K5iCQk5ZPt
LmqT+h3+1Q4sdLRjTruy3cXJ2cVBMqkC5i94STGV4WsxLyFfxy4SBsRH7zJuJcqf
gazIz+ibqWxPIGhounnJMChBviMBYNuLPXFyM9KS8faWbussa0qjKUJjDFGwyHad
lxGvU5dWFgdfClgdUH+NUCPLs8BZDfXqGLqak9hsFX7J+fYZR8a7K2rKhcsSysze
IQQCRTSYmNCZiwIMzevs40dMz5QUSTjscJklxwIDAQABAoIBAAyVzwMiLEpqhyNy
88N7osVTQxQKH3zp3l6eaA4SlocBgbCKeHw/t4y98uzNtEbASAYjTkHbd5ytRs/C
78Cckt75vfiQcIELXoUnLKfPfQ28q30+JyCmPcX7EZs/iqfIdL1rWFSHwEmJVkia
nik/uODA1gh4gU2EGgVIQEGXzNCv2RgTgmuyY+/4LbgEnUdMF+/umDhQd+o+nnL3
Ie0eJ7mTNPq78Dw6/21OcpE3j+yBIHGf5ZOHf5Qy+kBAytR7n+wzorkVYhbTvb4s
aWzHzmNBViQcum2SOaa/5I/HiG/Z4R2vnD53+bbjeLAsT/4OgUMdWziKOQbGbWwp
z+j/tekCgYEA8cfyOrbvkTLQHpC/1PC0GyrPGW+/5HKv34N+lCK4U+j6q5x7T7ia
kIacvW3/gPsmW0zcdty1RfgEKQXOT7sK7YN1yMwfRwHX7Ea9TW9ZPW/gnOlhwVJ0
Fx2SNESLmubi2cjEMayI9I++pDzwPMTLWNj53kgBhB/Qhw6+N74ScL0CgYEAymMm
JKVu3eNzooVIjS0wwlEpsteQZa1PI26QOyN/sr8wgbVrb/6P/dNc7Bl3YUMe0ZyR
ejyFo1bLsFemsWCZKWdgVOCQG1DqtHOPQSqkZPfYKfoMY9LWemyPk61CQDWzL3tg
L742V0iVPtYmtysKqagFFNeVML91duLWiobDwtMCgYAkl+2Kg2uI31bueVv/X5ry
zazgnbA+ZDlIK/+5bfPWB1oBJULokvkZzLXmWcKlA94PTXfEqazp9Rq0FsPd/2It
BouKI5LMTXQft6kpEiRAjzFArnX0K4WUhg49yO4UOMO20JMZLZLg6OyisPJvUB2y
ycwvn1hTZflKp6mUiDkERQKBgBUDyJEjkGh/1qD4f/kQyTBUJyVH1tmH7mC6eUV6
wSa5TXsacGZ3o1Hy4YIufsPdqVSQklaD9EhqmcncwBVI935iGpGVo8ECXOyR1z0o
BVvqlEp/iUvQN68MmLf31JpAOTPj9q/ea1wS0FRu/iQk1v2Y0bZBUF94ceT/VtGZ
frg7AoGBAI3iNhiZMQrq6j8kaEgDea+T1Ui0rGYIeD60TAuHfJ0a50Ga4rPp0u2p
G92Mk0sk2VGzZCkV6YRd/DJBXsqDAGeaEKzEnXiDBObUORDIo9SL3YhzosH191Ce
45ZXINAgovSzBcZfwStWjebUDw4v10Arc6ipkHGBPbK556S6wXGK
-----END RSA PRIVATE KEY-----
"""


#: CN=LemurTrust Unittests Class 1 CA 2018
INTERMEDIATE_CERT_STR = """\
-----BEGIN CERTIFICATE-----
MIIEGjCCAwKgAwIBAgIRAJ96dbOdrkw/lSTGiwbaagwwDQYJKoZIhvcNAQELBQAw
gaQxKjAoBgNVBAMMIUxlbXVyVHJ1c3QgVW5pdHRlc3RzIFJvb3QgQ0EgMjAxODEj
MCEGA1UECgwaTGVtdXJUcnVzdCBFbnRlcnByaXNlcyBMdGQxJjAkBgNVBAsMHVVu
aXR0ZXN0aW5nIE9wZXJhdGlvbnMgQ2VudGVyMQswCQYDVQQGEwJFRTEMMAoGA1UE
CAwDTi9BMQ4wDAYDVQQHDAVFYXJ0aDAeFw0xNzEyMzEyMjAwMDBaFw00NzEyMzEy
MjAwMDBaMIGnMS0wKwYDVQQDDCRMZW11clRydXN0IFVuaXR0ZXN0cyBDbGFzcyAx
IENBIDIwMTgxIzAhBgNVBAoMGkxlbXVyVHJ1c3QgRW50ZXJwcmlzZXMgTHRkMSYw
JAYDVQQLDB1Vbml0dGVzdGluZyBPcGVyYXRpb25zIENlbnRlcjELMAkGA1UEBhMC
RUUxDDAKBgNVBAgMA04vQTEOMAwGA1UEBwwFRWFydGgwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDR+qNdfNsLhGvgw3IgCQNakL2B9dpQtkVnvAXhdRZq
JETm/tHLkGvONWTXAwGdoiKv6+0j3I5InUsW+wzUPewcfj+PLNu4mFMq8jH/gPhT
ElKiAztPRdm8QKchvrqiaU6uEbia8ClM6uPpIi8StxE1aJRYL03p0WeMJjJPrsl6
eSSdpR4qL69GTd1n5je9OuWAcn5utXXnt/jO4vNeFRjlGp/0n3JmTDd9w4vtAyY9
UrdGgo37eBmi6mXt5J9i//NenhaiOVU81RqxZM2Jt1kkg2WSjcqcIQfBEWp9StG4
6VmHLaL+9/v2XAV3tL1VilJGj6PoFMb4gY5MXthfGSiXAgMBAAGjQjBAMA8GA1Ud
EwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEGMB0GA1UdDgQWBBQstpQr0iMBVfv0
lODIsMgT9+9oezANBgkqhkiG9w0BAQsFAAOCAQEASYQbv1Qwb5zES6Gb5LEhrAcH
81ZB2uIpKd3Ki6AS4fLJVymMGkUs0RZjt39Ep4qX1zf0hn82Yh9YwRalrkgu+tzK
rp0JgegNe6+gyFRrJC0SIGA4zc3M02m/n4tdaouU2lp6jhmWruL3g25ZkgbQ8LO2
zjpSMtblR2euvR2+bI7TepklyG71qx5y6/N8x5PT+hnTlleiZeE/ji9D96MZlpWB
4kBihekWmxuptED22z/tpQtac+hPBNgt8z1uFVEYN2rKEcCE7V6Qk7icS+M4Vb7M
3D8kLyWDubs9Yy3l0EWjOXQXxEhTaKEm4gSuY/j+Y35bBVkA2Fcyuq7msiTgrw==
-----END CERTIFICATE-----
"""
INTERMEDIATE_CERT = parse_certificate(INTERMEDIATE_CERT_STR)
INTERMEDIATE_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0fqjXXzbC4Rr4MNyIAkDWpC9gfXaULZFZ7wF4XUWaiRE5v7R
y5BrzjVk1wMBnaIir+vtI9yOSJ1LFvsM1D3sHH4/jyzbuJhTKvIx/4D4UxJSogM7
T0XZvECnIb66omlOrhG4mvApTOrj6SIvErcRNWiUWC9N6dFnjCYyT67JenkknaUe
Ki+vRk3dZ+Y3vTrlgHJ+brV157f4zuLzXhUY5Rqf9J9yZkw3fcOL7QMmPVK3RoKN
+3gZoupl7eSfYv/zXp4WojlVPNUasWTNibdZJINlko3KnCEHwRFqfUrRuOlZhy2i
/vf79lwFd7S9VYpSRo+j6BTG+IGOTF7YXxkolwIDAQABAoIBAQC8dTuSeLEQUTWR
cVlIr043RpkPv1zF/BGm3PZaOAB6GztMJ4CcN27KkNmEsMoOdKq1QgaAnT+GpMX0
RjZpd3omyJi7JAPAVdavQNjm/RXjWRqZFlVw/LxDXbOjcc+IXQOk73rEdLBcvKT5
ZRjirzPev5IE49AF/0/0VYPqSHHEXL1HMWy5Q7KZU/C4Yp8em2l3UAh1/nLI2L+U
iw6DxBhBbdsc2vD4dd4UUQmznBfvdBOiejKs9DYIDzmTrGI2lH0VUU6PVzb9LKJ3
UtlIsjOO0FdJxXhkjsDCcF4eEMhO4qOfVJDcl0YYsPLjM0t4IVfe2C0b3Hd37hhF
b3ux0YoBAoGBAPWCPBepUdtiiMM21dLFPuy/d9/C3k8xTD23aO8zupwnGD1zz8OY
1GzsCtR9me0nIbHGxT+Unovuxh2JYQgrFpAFsG/izL8SpkDeT3hJDPY8PLrhGqMS
RBcYYgZ+1aNZTPZRKDjTG7PlwkcDt8VzQYYl87MBtDpPmdYkWYPnS+5XAoGBANrz
uSjbbTEX4a3WGsot9WzyhML11WgsdMgbqSWLMEmj2guwm4jn3XdqA+6nZAUJHgPI
Ir5l2E3zWTdw5pZ0+IkQnj/OJP2OLqS+msVMl89PHJjtPyB2LVjCg+Z/vfm2ar5S
RnQ/AoR5cSXctiL9wJbJBidfZeEpXBSeKN/SW6/BAoGAXaQ4EXpWq4wQyAzRT9xG
HP0G1wU30BLolp2vW5Vqdwb+Wuoic+OGGqmJk/T4Uhlb47gCIjcopg0D6d4tcXUl
3Pcejf5+w950JUfmHeYXGJBvRYR4qXxdFkYJlZqpF+4Gyei4o7v51Astp/KGFLza
YDV3l25t9NPJxIEG16XQM28CgYEAyT3yFYd42QKmPuznOqT7SuOs+rSRLWqO+83Q
rd08yLJ9Gvl8O11BxRv/+T6JQ8eZeshchrt9EEh22+o9RlTEitZnXSXQAezJGkrG
XkmDzttb4YNN3jxAebBvI1COABKWEc/1SasQWUp1oOM31Pl+JhkmOtIIBefJ5nlo
ADCMbQECgYBdpg/2J58JOB0NhFFUDh3+6+bzZIciT7BYZ8zYBej5DR6kd4Inkvvl
JxOlYIKSew5uyi7i2po7fBFRhKuyfpNMBYK01ObrgJNZELbqVgYvKw1HEqqtgExa
eMVHHbWm1CpGO294R+vMBv4jcuhIBOx63KZE4VaoJuaazF6TE5czDw==
-----END RSA PRIVATE KEY-----
"""


#: CN=san.example.org, issued by LemurTrust Unittests Class 1 CA 2018
SAN_CERT_STR = """\
-----BEGIN CERTIFICATE-----
MIIESjCCAzKgAwIBAgIRAK/y20+NLU2OgPo4KuJ8IzMwDQYJKoZIhvcNAQELBQAw
gacxLTArBgNVBAMMJExlbXVyVHJ1c3QgVW5pdHRlc3RzIENsYXNzIDEgQ0EgMjAx
ODEjMCEGA1UECgwaTGVtdXJUcnVzdCBFbnRlcnByaXNlcyBMdGQxJjAkBgNVBAsM
HVVuaXR0ZXN0aW5nIE9wZXJhdGlvbnMgQ2VudGVyMQswCQYDVQQGEwJFRTEMMAoG
A1UECAwDTi9BMQ4wDAYDVQQHDAVFYXJ0aDAeFw0xNzEyMzEyMjAwMDBaFw00NzEy
MzEyMjAwMDBaMHgxGDAWBgNVBAMMD3Nhbi5leGFtcGxlLm9yZzEYMBYGA1UECgwP
RGFuaWVsIFNhbiAmIGNvMRcwFQYDVQQLDA5LYXJhdGUgTGVzc29uczELMAkGA1UE
BhMCRUUxDDAKBgNVBAgMA04vQTEOMAwGA1UEBwwFRWFydGgwggEiMA0GCSqGSIb3
DQEBAQUAA4IBDwAwggEKAoIBAQDImvQXKcqWVFPcSaJJ83RKfgHr0BPd10gMpSJV
44vNGZWEv0/5lVrbuoTcM9iCQwRYepz2h09VHfwCOGGpwzGvnxeCicc5ZCj22Krl
seBDo02drBQQQor8MZaNUqPK+R3+DWfRMLuACJmt85pPnc8SU6Z1m0yBSRrAxi8C
TvYrurqn+/VXWJBhCwrrKt3chdo9gzQ4hh6EXEGBTDIQykermJgk2L8I39PrH+pN
c5NhCtV/mVlMoz/jZdjQem6S9E8nRe+X7qZVkTnM3HojugSjuGE9rjT3ReAQB6f5
EApKp48ORQl+zzjUU+ME1vwIw5LeVjoGPgAfdM0AT8b11m1DAgMBAAGjgZ4wgZsw
DAYDVR0TAQH/BAIwADATBgNVHSUEDDAKBggrBgEFBQcDATAOBgNVHQ8BAf8EBAMC
BaAwHQYDVR0OBBYEFPMfkyOR6taOKARGUn1zyauOeOhAMEcGA1UdEQEB/wQ9MDuC
D3Nhbi5leGFtcGxlLm9yZ4IQc2FuMi5leGFtcGxlLm9yZ4IWZGFuaWVsLXNhbi5l
eGFtcGxlLm9yZzANBgkqhkiG9w0BAQsFAAOCAQEAJer6tDWlcc4gDvZEbPNpFPKY
kPqww6WtVKrsyPQyucmP7arFx+kUulkZN6GY6FyIao7zQPrHU3GqtPXt/lR++wzz
bnj+iHONNoAY5TZLycPXAW7pn8UCvdQzkyhMzCB1aRkRS/Tr0/sC0T5lYux42dQG
rTUxVG7Umr4jq8hKEElNIwxF+3kkfzztICZXJtzmVRAz4XpmXmyMcZOOXh3F7z04
kePn3ztNEJNuGK0qMnTJlL7T2a9v+Q29YhIiNqCFdoALJbzJmEj3+QgcLFJh3KjY
J4WEmpGK7FylxmZLrya12SxPMA8A60hMPeWH90xRS8SJfd57K5oCluGK14X+og==
-----END CERTIFICATE-----
"""
SAN_CERT = parse_certificate(SAN_CERT_STR)
SAN_CERT_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAyJr0FynKllRT3EmiSfN0Sn4B69AT3ddIDKUiVeOLzRmVhL9P
+ZVa27qE3DPYgkMEWHqc9odPVR38AjhhqcMxr58XgonHOWQo9tiq5bHgQ6NNnawU
EEKK/DGWjVKjyvkd/g1n0TC7gAiZrfOaT53PElOmdZtMgUkawMYvAk72K7q6p/v1
V1iQYQsK6yrd3IXaPYM0OIYehFxBgUwyEMpHq5iYJNi/CN/T6x/qTXOTYQrVf5lZ
TKM/42XY0HpukvRPJ0Xvl+6mVZE5zNx6I7oEo7hhPa4090XgEAen+RAKSqePDkUJ
fs841FPjBNb8CMOS3lY6Bj4AH3TNAE/G9dZtQwIDAQABAoIBAQCxN3J7JAg8VbLf
4IzmF5ScWkUINYHXcN/Ni/SRO7u9LOTRqNDWBAOIKXZFseeK6/li0K7pew+yehKv
Q2/DsRSruTfjsiO1p64oo7AVytX76sAekm4HD0IJGSWPI3pfTUQZs24Ld6msqexZ
p+Kigx7zacKcEt27OQHRW0McHvWKGpCzc+G9o8hlYumtnTnR8kP4bYG4MpCVtZdt
ZuQr9QHEH7omQzWedLHICqGLP8WBu+lMY3bPM/gLgBSy2f8CP5MBy7xUUSTgolCc
ZZIt2H2cCStfb3y61WvDHX/bZ7B/a0lDWKHUK2f9Du5ENOWAAsaIUCPGrFwMFM1n
ANPtYIUBAoGBAP7SXzTcsHx0Iy1TMqluQxZNL7Up6dHksZFEO8zAwmg6Z3VHsXjc
3ovst1gQRWUzEhc2Soun8KbZ4ZVhApHpkxg+lLio2A4mLm7xf6ASsPwkwUCwUBYP
zSt56oopQ6BIc84ZDNe5QZY9OziRyHRc0SgVhuoK1i2t832kUii/aWmTAoGBAMmI
aA6vDlojHnyhvNCS/v+aOEjNyW7LJjDhNK6qTKZF7FeCSjTLxzJJ6XddQjLXnjVa
aF1I0dYPLQfjbeDaM6pKyg4l0pnN70qh9YgFCCIxU0dIqL2v0a057JILwlC4ZU8z
rmQEP3DROGGi50r74/SoYMBVm6r/6opYkThF+HuRAoGBAIHxrXM7hxQv9TBL2O3l
uHhK7CUqNn4+bP5zGTuUoI6eGdwIr0u+9g3MrMJPqdOtc3A601DcVy/+s7aFPdZC
kiwu3ZA9KdAtUEhrBnYOkgpCg/oE7xIRBMNC7IN//2hhCgzzYUUwx21h1C1Iyjvs
iQwzzhTTadzpc92CShNVaN/ZAoGBAKwG+fv+xdt/OtjcHpZTw8NfW0gaESW31yPG
OPgXelI8QZ/5IWqrv59XpCg1vPo1P2D/iTKHpEZ6sc+X/QUAfTWRnaQx+PE87lPg
p/uxf93gCNxCU3eHiw248g1AaGAK5r+St/u7/INKtDvzmEdTeKQwzlWfPb/br9Lk
AyHr6E1hAoGAN375PaykO+webBV9GkUwCcs1wTmDFjWKuaCVk9qvj8qavr1HOarb
ZolDBFYQSUUcOJHE9QRg7zDWTjI+Av670rXtTsREs0yMkdHhF/aRD7FJoBvO/7v/
tqdgqMHlJ0YPL/8/6sTMasepIqmAkQgFINzDskHubBBEPfHKqF0KQA4=
-----END RSA PRIVATE KEY-----
"""

WILDCARD_CERT_STR = """\
-----BEGIN CERTIFICATE-----
MIIEJDCCAwygAwIBAgIPK/QvcZhAY7VPU7Ek/nCDMA0GCSqGSIb3DQEBCwUAMIGn
MS0wKwYDVQQDDCRMZW11clRydXN0IFVuaXR0ZXN0cyBDbGFzcyAxIENBIDIwMTgx
IzAhBgNVBAoMGkxlbXVyVHJ1c3QgRW50ZXJwcmlzZXMgTHRkMSYwJAYDVQQLDB1V
bml0dGVzdGluZyBPcGVyYXRpb25zIENlbnRlcjELMAkGA1UEBhMCRUUxDDAKBgNV
BAgMA04vQTEOMAwGA1UEBwwFRWFydGgwHhcNMTcxMjMxMjIwMDAwWhcNNDcxMjMx
MjIwMDAwWjB9MRswGQYDVQQDDBIqLndpbGQuZXhhbXBsZS5vcmcxETAPBgNVBAoM
CFBsYXl0ZWNoMRkwFwYDVQQLDBBJbmZyYSBPcGVyYXRpb25zMQswCQYDVQQGEwJF
RTERMA8GA1UECAwISGFyanVtYWExEDAOBgNVBAcMB1RhbGxpbm4wggEiMA0GCSqG
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQCoT8Ak5kynUzosBvP8hCnP4hGMAtgHLcHG
UBWug4BofAhxxBrZW3UteoQzNznK5jz0hy2azqnz3/9q5N/FKwHxfMY/VEHPXyYK
QsZuSdVceJ/EHL+MLx+uisIRJstV8fC5oYRfg74m07ZED7NM4EerJTxKZAy7UuSM
L65i/LEChPzjLN46GcUEuC2O03nZtFTPvN9j7vzen9/qIzs1TGQukOn4z5l2GuAx
RCEfBl3IrnvSY+npGARPJsXSymXCCP3ntzq6I6iRHuZf+QETZtiMR1TCNZRTqcc2
LxWn+W5N18yyXvUcVMfrg4jzEWKHuhwInoiH1pu/myyKrnoIi4nTAgMBAAGjdjB0
MBMGA1UdJQQMMAoGCCsGAQUFBwMBMA4GA1UdDwEB/wQEAwIFoDAMBgNVHRMBAf8E
AjAAMB0GA1UdDgQWBBRR9Q9DHJRPt69Qm8lir4iJfOmJ4TAgBgNVHREBAf8EFjAU
ghIqLndpbGQuZXhhbXBsZS5vcmcwDQYJKoZIhvcNAQELBQADggEBAMm2DiYfGLve
r/gCtYgXKkRmbuv57PmAUm52w5l4hjxssdUwq4Wn4T+K0+Sqp3IzcNhEaIqPB+bG
8rIbJLBiiDPbSUZC0DbvlXihk7FHjqmrbVFwNmkWNywLhB1qOlp0kQH+w9lDWA1p
y99P0Bxcot66scbiaag0i0AUpkRKbUG+v+VGXdPrJrWE+63ROhWQMmQNiUlZ6QGO
45tUSn//MuUpJiJVkUVR1fSbCpHQj2mHiuhShOmatmh5e1ISwVP19cX64Gr6djlY
wKJqcmw7WDjl+T+y7luJWw4UqI7s7hY6Y9RQVh61L4eV8CIma3NmTaQCSgR3tCxh
d4FCKAE8+Lw=
-----END CERTIFICATE-----
"""
WILDCARD_CERT = parse_certificate(WILDCARD_CERT_STR)
WILDCARD_CERT_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAqE/AJOZMp1M6LAbz/IQpz+IRjALYBy3BxlAVroOAaHwIccQa
2Vt1LXqEMzc5yuY89Ictms6p89//auTfxSsB8XzGP1RBz18mCkLGbknVXHifxBy/
jC8frorCESbLVfHwuaGEX4O+JtO2RA+zTOBHqyU8SmQMu1LkjC+uYvyxAoT84yze
OhnFBLgtjtN52bRUz7zfY+783p/f6iM7NUxkLpDp+M+ZdhrgMUQhHwZdyK570mPp
6RgETybF0splwgj957c6uiOokR7mX/kBE2bYjEdUwjWUU6nHNi8Vp/luTdfMsl71
HFTH64OI8xFih7ocCJ6Ih9abv5ssiq56CIuJ0wIDAQABAoIBAHpE3SexKbRQMK01
K9+gPyOmberRUg/8/IzNNsL9ArZkjFnhBUQrPXeZThpKnzA3i8ZzwPx571qbudf0
hl6cfJ/qbbYpxlkYHPFNSwtplZbEhgOYgsoanaBVat+81/AKfz7LB/e/I87e88SD
x1QshcPdm+vKvLkEYcU5Ci0ctpZFyjgqWAVdsaEmstSpygOsU/CExiiq20MuGXQV
lfRpYqmA0D1LicN6t0rGRNLUHWzhZS5s1ZHD8oR5bgtlcxvOSDm81ROfV1obAQRo
RyCeYG9Juo2BisyuG5RsKuzfWvP6goxXdGD2uTOj7rdMYRfnUzsz4QXkzdA+IEE9
qmv9gsECgYEA0gYoSVwF+koYL8SURMLbQPdmVBiTSxZQytSaFTl9WWYUvyFJ/R0c
xmuMjfVvnxuMUa6qHcaOt9Gjq0pAp2T10/8B+fB8XAJ0bxl6DKArxIONx7W1T8RX
SdEAWF77eRlSPAD4dfAyFIjPzCH4l98nX84sRk+GiusLGhm5MdwTS2ECgYEAzSgB
H33YIfPMW7Mh9R7QpfQRyda9Ikb8pGDegprTLp9SDLU0zCZ3aPmSN3iVrGThwcf1
olnx5g8ZK9qiLLIUctxJWeK/EO2HAii/fmasJfq4zI0xBflkX25V+BbZRqU8GDa0
dLpOcr1cIEFAqpZ182O1uXAJdGzkVv4LN5Iq9bMCgYBuYAIIG66gjRQM9pidUnJ7
wAktJQUzrvSiw/x+LwprUzSQBeSmewhGVvs1F8mjqoyh2NNadqFGhYwoVwuHbY2r
7haRzgrtJ/Uc9hyoSfz2d9SpIhu5YgwlpQszZiduyxnmovPwt1z6YbQjKa9F0WcV
+HpYMS8aDtB01RP42hnhwQKBgHDg8PU9zZyowqk1v5pZ8R1OVDdE4t2oRzu+XM9p
loaRfJinXzxwccUdhFjnDRtEin6PodRJPvKBHi1l51NGTEACeo1tWAldV6pVdz96
CIABGorZqL6LwLFNSRnuoG/hXFZKSzHqjF1PWRAaNxVlIdLf6s30Gg+oFl7S+qMB
1odHAoGAQqPWDTSBVhbMIzXXoGGjIx08WG9xuNqRyQ6fjekSporXisoej1XB+pYA
wZF7+p71qUsrVrg+j7SRm8pFsR79nvshQImzaLGOCLUsdHZfcKjfy8D7wB6T7AmF
gt+hqNmTFkpLkvaze7sBEwRWRU0/RWpZLDmx3+zvRXPw1lQmB1Q=
-----END RSA PRIVATE KEY-----
"""


INVALID_CERT_STR = """
-----BEGIN CERTIFICATE-----
MIIEFTCCAv2gAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwgYwxCzAJBgNVBAYTAlVT
MQswCQYDVQQIDAJDQTEQMA4GA1UEBwwHQSBwbGFjZTEXMBUGA1UEAwwObG9uZy5s
aXZlZC5jb20xEDAOBgNVBAoMB0V4YW1wbGUxEzARBgNVBAsMCk9wZXJhdGlvbnMx
HjAcBgkqhkiG9w0BCQEWD2ppbUBleGFtcGxlLmNvbTAeFw0xNTA2MjYyMDM2NDha
Fw0xNTA2MjcyMDM2NDhaMGkxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEQMA4G
A1UEBxMHQSBwbGFjZTEQMA4GA1UEChMHRXhhbXBsZTETMBEGA1UECxMKT3BlcmF0
aW9uczEUMBIGA1UEAxMLZXhwaXJlZC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQCcSMzRxB6+UONPqYMy1Ojw3Wi8DIpt9USnSR60I8LiEuRK2ayr
0RMjLJ6sBEgy/hISEqpLgTsciDpxwaTC/WNrkT9vaMcwfiG3V0Red8zbKHQzC+Ty
cLRg9wbC3v613kaIZCQCoE7Aouru9WbVPmuRoasfztrgksWmH9infQbL4TDcmcxo
qGaMn4ajQTVAD63CKnut+CULZIMBREBVlSTLiOO7qZdTrd+vjtLWvdXVPcWLSBrd
Vpu3YnhqqTte+DMzQHwY7A2s3fu4Cg4H4npzcR+0H1H/B5z64kxqZq9FWGIcZcz7
0xXeHN9UUKPDSTgsjtIzKTaIOe9eML3jGSU7AgMBAAGjgaIwgZ8wDAYDVR0TAQH/
BAIwADAOBgNVHQ8BAf8EBAMCBaAwFgYDVR0lAQH/BAwwCgYIKwYBBQUHAwEwHQYD
VR0OBBYEFKwBYaxCLxK0csmV319rbRdqDllWMEgGA1UdHwRBMD8wPaA7oDmGN2h0
dHA6Ly90ZXN0LmNsb3VkY2EuY3JsLm5ldGZsaXguY29tL2xvbmdsaXZlZENBL2Ny
bC5wZW0wDQYJKoZIhvcNAQELBQADggEBADFngqsMsGnNBWknphLDvnoWu5MTrpsD
AgN0bktv5ACKRWhi/qtCmkEf6TieecRMwpQNMpE50dko3LGGdWlZRCI8wdH/zrw2
8MnOeCBxuS1nB4muUGjbf4LIbtuwoHSESrkfmuKjGGK9JTszLL6Hb9YnoFefeg8L
T7W3s8mm5bVHhQM7J9tV6dz/sVDmpOSuzL8oZkqeKP+lWU6ytaohFFpbdzaxWipU
3+GobVe4vRqoF1kwuhQ8YbMbXWDK6zlrT9pjFABcQ/b5nveiW93JDQUbjmVccx/u
kP+oGWtHvhteUAe8Gloo5NchZJ0/BqlYRCD5aAHcmbXRsDid9mO4ADU=
-----END CERTIFICATE-----
"""
INVALID_CERT = parse_certificate(INVALID_CERT_STR)


EXTERNAL_VALID_STR = """
-----BEGIN CERTIFICATE-----
MIIFHzCCBAegAwIBAgIQGFWCciDWzbOej/TbAJN0WzANBgkqhkiG9w0BAQsFADCB
pDELMAkGA1UEBhMCVVMxHTAbBgNVBAoTFFN5bWFudGVjIENvcnBvcmF0aW9uMR8w
HQYDVQQLExZGT1IgVEVTVCBQVVJQT1NFUyBPTkxZMR8wHQYDVQQLExZTeW1hbnRl
YyBUcnVzdCBOZXR3b3JrMTQwMgYDVQQDEytTeW1hbnRlYyBDbGFzcyAzIFNlY3Vy
ZSBTZXJ2ZXIgVEVTVCBDQSAtIEc0MB4XDTE1MDYyNDAwMDAwMFoXDTE1MDYyNTIz
NTk1OVowgYMxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDQUxJRk9STklBMRIwEAYD
VQQHDAlMb3MgR2F0b3MxFjAUBgNVBAoMDU5ldGZsaXgsIEluYy4xEzARBgNVBAsM
Ck9wZXJhdGlvbnMxHjAcBgNVBAMMFXR0dHQyLm5ldGZsaXh0ZXN0Lm5ldDCCASIw
DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALwMY/yod9YGLKLCzbbsSUBWm4ZC
DfcgbUNL3JLtZaFCaOeUPLa4YNqty+9ACXBLYPNMm+dgsRHix8N2uwtZrGazHILK
qey96eSTosPsvKFt0KLNpUl8GC/YxA69L128SJgFaaq5Dr2Mp3NP0rt0RIz5luPj
Oae0hkGOS8uS0dySlAmfOw2OsJY3gCw5UHcmpcCHpO2f7uU+tWKmgfz4U/PpQ0kz
WVJno+JhcaXIximtiLreCNF1LpraAjrcZJ+ySJwYaLaYMiJoFkdXUtKJcyqmkbA3
Splt7N4Hb8c+5aXv225uQYCh0HXQeMyBotlaIrAddP5obrtjxhXBxB4ysEcCAwEA
AaOCAWowggFmMCAGA1UdEQQZMBeCFXR0dHQyLm5ldGZsaXh0ZXN0Lm5ldDAJBgNV
HRMEAjAAMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYB
BQUHAwIwYQYDVR0gBFowWDBWBgZngQwBAgIwTDAjBggrBgEFBQcCARYXaHR0cHM6
Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5bWNi
LmNvbS9ycGEwHwYDVR0jBBgwFoAUNI9UtT8KH1K6nLJl7bqLCGcZ4AQwKwYDVR0f
BCQwIjAgoB6gHIYaaHR0cDovL3NzLnN5bWNiLmNvbS9zcy5jcmwwVwYIKwYBBQUH
AQEESzBJMB8GCCsGAQUFBzABhhNodHRwOi8vc3Muc3ltY2QuY29tMCYGCCsGAQUF
BzAChhpodHRwOi8vc3Muc3ltY2IuY29tL3NzLmNydDANBgkqhkiG9w0BAQsFAAOC
AQEAQuIfyBltvCZ9orqNdS6PUo2PaeUgJzkmdDwbDVd7rTwbZIwGZXZjeKseqMSb
L+r/jN6DWrScVylleiz0N/D0lSUhC609dQKuicGpy3yQaXwhfYZ6duxrW3Ii/+Vz
pFv7DnG3JPZjIXCmVhQVIv/8oaV0bfUF/1mrWRFwZiBILxa7iaycRhjusJEVRtzN
Ot/qkLluHO0wbEHnASV4P9Y5NuR/bliuFS/DeRczofNS78jJuZrGvl2AqS/19Hvm
Bs63gULVCqWygt5KEbv990m/XGuRMaXuHzHCHB4v5LRM30FiFmqCzyD8d+btzW9B
1hZ5s3rj+a6UwvpinKJoPfgkgg==
-----END CERTIFICATE-----
"""
EXTERNAL_CERT = parse_certificate(EXTERNAL_VALID_STR)


INTERNAL_CERTIFICATE_A_STR = """
-----BEGIN CERTIFICATE-----
MIIDazCCAlOgAwIBAgIBATANBgkqhkiG9w0BAQsFADB5MQswCQYDVQQGEwJVUzET
MBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJTG9zIEdhdG9zMRYwFAYDVQQK
DA1OZXRmbGl4LCBJbmMuMRMwEQYDVQQLDApPcGVyYXRpb25zMRQwEgYDVQQDDAtB
Y29tbW9uTmFtZTAeFw0xNjA2MjkyMjE0NDdaFw0zNjA2MjkyMjE0NDdaMHkxCzAJ
BgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlMb3MgR2F0
b3MxFjAUBgNVBAoMDU5ldGZsaXgsIEluYy4xEzARBgNVBAsMCk9wZXJhdGlvbnMx
FDASBgNVBAMMC0Fjb21tb25OYW1lMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEAtkyvL6EqSgYSJX11635Hb8FBG/8Wey6C2KtG7M+GXvGCsSmfNqQMeZdf
W9Avxelkstp5/K+ilVJJ2TJRelu1yVUUkQcrP7imgf7CxKQAnPz2oXQImLFbm7OS
1zKA+qwtLGrId3vVQaotUtdI+wxx0YE66pyfOhQJsVOeuYwG8CCxnAj/lXeNLA1t
n39A8FLfj9nxjvZWWm2z8qXO2IYOWEMOOel1zixhypeJoTD2cJHDKNlUnXN4q5ej
psD4ehLFXIPXsKJv5XOtNYB9UHB3moXlEOuKAquRzBOfTP+rUYyfbHmzCN4eXekp
R6vze49hlg8QdCNjVY6jHRrOuVKGuwIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAt
rE2Ee6a0zRlJHiuP5Zr61s6ZnwIsPN5sjo3pFJ/goHeNWbq+02FUJLXROtxSMlo8
jLYpnQbm3Qoyd0KjGn9myP1vqBL6Yzf9dRI2li9XYmavxU7OK/KJtBo/Wnw3DVT5
jxYrn4YKJU9+T0hr57bWUQ7HjMNojwBcgglzPN9KOtfTfbPEUIeoRpCjeyjwBUSN
nrTDiYPV+XI4LAyDmuR7esSvm2+0h6C0dmUbVspkxBaKFEYUKIYaZbEFEBsyZGri
qDIyu9HSvu2MJ2lVxfMNsW+IYG74DOqJQsIFP+7hrfdPoMGm4GvAiHR1IuSmq+sf
L0Ew8hy0GG3nZ6uXLW7q
-----END CERTIFICATE-----
"""


INTERNAL_PRIVATE_KEY_A_STR = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAtkyvL6EqSgYSJX11635Hb8FBG/8Wey6C2KtG7M+GXvGCsSmf
NqQMeZdfW9Avxelkstp5/K+ilVJJ2TJRelu1yVUUkQcrP7imgf7CxKQAnPz2oXQI
mLFbm7OS1zKA+qwtLGrId3vVQaotUtdI+wxx0YE66pyfOhQJsVOeuYwG8CCxnAj/
lXeNLA1tn39A8FLfj9nxjvZWWm2z8qXO2IYOWEMOOel1zixhypeJoTD2cJHDKNlU
nXN4q5ejpsD4ehLFXIPXsKJv5XOtNYB9UHB3moXlEOuKAquRzBOfTP+rUYyfbHmz
CN4eXekpR6vze49hlg8QdCNjVY6jHRrOuVKGuwIDAQABAoIBACYPnqfwGzc3S0Se
jCctx1Zy39grixMO4+y+3eEFdwWNoP7CNOagm6YrT5KIxeCpWQfqi3uRY/2PH7IE
SnSkfzDY3aFmAMaeE82iViHeJ+6e9hNBeaX/qaO5e1gIyFsN5aSXauFfbmf2Ut4v
6qHXuE/Ijnd7WdczZc6rKcGNlck+f/QtsZhYEYbgHT3Nrt0ztlvkdrcyRIxZTeS7
7gvVWrVv6rviTobi/ZkeM9pqe5bbLuWgb/ArvI52pJwaUcz9LPGo+miank6e4gAd
cTudoREtBKVgXROhTSz33mdjjUTCDGdtILTztDSgLpJXYT0w2h1zmfV7t4tztzzQ
xW5LVCECgYEA33YG/gaZbfH6szC/heilojelrIG+n7GjsqpfMqGFofYNBAswUC3w
qZdeXxqGZEXC8mx8CufDhC50vJv353WAHaFFJcwy2QeGvHfPAZ4ZQ68o9XLeva4t
M6+ZtOiaK8u/mzxq43Jj7FbXmxxlJXY3B0uWdWpKGsPRTmSaUw0lKPECgYEA0NhG
74C6zRgHY2Eq2Qq7+NtlvpzUtVtalhiDoCEpDMhjzLUTBNy6yMsSdP8SyCy9O7Ng
rrXJdgKHvpjnJyUvB3hhEAurPIPWJArEfEHAF+V8mHY8f58xZqgHRsYsH3tWHYx4
2lzmposTES5KKV4xsYbjjyzXX+WNdaOkC4JBCmsCgYEA3j2JKL0xfMordmlmIWzG
xnWnnNCQ4EwQrVGKSlWgDPsj6MCj9Sorbs9veRBtVm6XOvkvyLzFk8GMMkTAIf+X
QmCw362daIF2vBw/0bEGGW2sQ6hR5L3EkOH08ZpgMmx6DI7jE4Ah5txbpBVydvaC
Ngw0AGSMfOABW4DshurM6VECgYEAxeH3rJ2r4gL/lSGPaOGr5At2Z1rQjRqHRarq
pQJmk+8X6PI1mCjRbspDrcm2cSc7EmNPm5sxzXhuSKE2fLfVzN06EusLkCZW9AWj
0Ry3t6zBFvEJN9+N/nf9lQjW6+mAWjUsmbLm9SzXnzLeID5ZFZ365kGVvQ6Tr8Cj
AiikGgsCgYEAlYGNwBKWClm797YVyPhmqrFX4T9Hpxc7oC3vVwd96tAbLlSrW8r5
o6ynBW1bG+qfjx9GyThgudvRtB+0vTSShrT5GftLCyMtOiYSHkGEvMOGFBuowzoz
3i841gR9+cwA0S1hy7fC0PDmTo0xC91JocwesPQ023MmECPfu6Frzog=
-----END RSA PRIVATE KEY-----
"""


CSR_STR = """
-----BEGIN CERTIFICATE REQUEST-----
MIIC1zCCAb8CAQAwczEUMBIGA1UEAwwLQUNvbW1vbk5hbWUxFTATBgNVBAoMDG9y
Z2FuaXphdGlvbjEOMAwGA1UECwwFZ3VuaXQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
DApDYWxpZm9ybmlhMRIwEAYDVQQHDAlzb21ld2hlcmUwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDNnY+Ap+V9+Eg/PAtd7bq27D7tDvbL10AysNUSazy7
gJyHfJyE3oiXm28zjFNzRQ35qhsCFpWg8M36FpdP9fIFG9sVXV/ye+YNBkZ2aTJi
RnbErZcy8qc+2MRd2JKE9g0pISp9hAEeEPLTwSoGqf5VqOaBehBqL5OKNUr7JAxV
TIH1oVU87w/6xg/WsUiyPo49WXxF/3DZNP1UOTYiffxIiARhTb9EtlXpt5iOlic3
w/vBX6qsH++XJIus2WE+ABlAVUQTCvc6bgpu4zjc8nlm3ClqkAKcxn2ubEder+Fh
hagMYGsbYG+/IWrKYN6S0BjE26tNMiOlmIebimjEdFpnAgMBAAGgHzAdBgkqhkiG
9w0BCQ4xEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAE5OKI/n
b1ZRJDL4SpjWggRjfwBdYmb96lGH0aGDoVUP9UUusLzpWLtutkgr9Hh29agSsLZF
j535NeXHf+Jc4UyR288WQVJthgAT1e5+jBNPxz4IcTnDW7ZMJLGm495XaKi6Krcg
+8Qn2+h04jBTbN2Z9+MXGak0B8ycrbDx/FYL4KgBJRvS805d43zC6L1aUfRbpZgN
QeQoBdLhFNB1kAYSWCyETwRQOeGEphBJYBPcXsQVBWbMtLpbhjRZ1uTVZEFIh8Oa
zm3Cn4Ul8DO26w9QS4fmZjmnPOZFXYMWoOR6osHzb62PWQ8FBMqXcdToBV2Q9Iw4
PiFAxlc0tVjlLqQ=
-----END CERTIFICATE REQUEST-----
"""
