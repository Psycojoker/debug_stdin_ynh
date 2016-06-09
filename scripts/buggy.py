import pexpect

openssl = pexpect.spawn("openssl req -out CSR.csr -new -newkey rsa:4096 -nodes -keyout client.key", cwd=".", timeout=120)

openssl.expect("Country Name \(2 letter code\) \[AU\]:")
openssl.sendline(".")
openssl.expect("State or Province Name \(full name\) \[Some-State\]:")
openssl.sendline(".")
openssl.expect("Locality Name \(eg, city\) \[\]:")
openssl.sendline(".")
openssl.expect("Organization Name \(eg, company\) \[Internet Widgits Pty Ltd\]:")
openssl.sendline(".")
openssl.expect("Organizational Unit Name \(eg, section\) \[\]:")
openssl.sendline(".")
openssl.expect("Common Name \(e.g. server FQDN or YOUR name\) \[\]:")
openssl.sendline("debug certificat that is useless")
openssl.expect("Email Address \[\]:")
openssl.sendline(".")
openssl.expect("A challenge password \[\]:")
openssl.sendline("")
openssl.expect("An optional company name \[\]:")
openssl.sendline("")

openssl.interact()
