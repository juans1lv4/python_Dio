email = input('Digite seu email: ').strip()

if '@' in email and ('gmail.com' in email or 'outlook.com' in email) and not email.startswith('@') and not email.endswith('@') and ' ' not in email:
    print('Email validado')
else:
    print('email invalido')