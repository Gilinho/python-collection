import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your@gmail.com', 'your-password')
mail.list()
mail.select('inbox')

label, data = mail.search(None, 'ALL')

for num in data[0].split():
    label, data = mail.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])

mail.logout()
