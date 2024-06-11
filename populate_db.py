from Users.models import User, Client

# Создаем пользователей
user1 = User.objects.create_user(username='petrov', password='pass123', full_name='Петров Петр Петрович')
user2 = User.objects.create_user(username='sidorov', password='pass123', full_name='Сидоров Сидор Сидорович')

# Создаем клиентов
Client.objects.create(account_number=1, last_name='Иванов', first_name='Иван', middle_name='Иванович', birth_date='1980-01-01', inn='123456789012', responsible_full_name=user1, status='Не в работе')
Client.objects.create(account_number=2, last_name='Петрова', first_name='Мария', middle_name='Сергеевна', birth_date='1990-02-02', inn='987654321098', responsible_full_name=user2, status='Не в работе')
Client.objects.create(account_number=3, last_name='Смирнов', first_name='Алексей', middle_name='Алексеевич', birth_date='1985-03-03', inn='234567890123', responsible_full_name=user1, status='Не в работе')
Client.objects.create(account_number=4, last_name='Кузнецова', first_name='Ольга', middle_name='Николаевна', birth_date='1975-04-04', inn='345678901234', responsible_full_name=user2, status='Не в работе')
Client.objects.create(account_number=5, last_name='Попов', first_name='Михаил', middle_name='Викторович', birth_date='1965-05-05', inn='456789012345', responsible_full_name=user1, status='Не в работе')
Client.objects.create(account_number=6, last_name='Волкова', first_name='Елена', middle_name='Дмитриевна', birth_date='1995-06-06', inn='567890123456', responsible_full_name=user2, status='Не в работе')
Client.objects.create(account_number=7, last_name='Соколов', first_name='Дмитрий', middle_name='Иванович', birth_date='1982-07-07', inn='678901234567', responsible_full_name=user1, status='Не в работе')
Client.objects.create(account_number=8, last_name='Лебедева', first_name='Анастасия', middle_name='Павловна', birth_date='1998-08-08', inn='789012345678', responsible_full_name=user2, status='Не в работе')
Client.objects.create(account_number=9, last_name='Морозов', first_name='Виктор', middle_name='Сергеевич', birth_date='1978-09-09', inn='890123456789', responsible_full_name=user1, status='Не в работе')
Client.objects.create(account_number=10, last_name='Орлова', first_name='Екатерина', middle_name='Алексеевна', birth_date='1987-10-10', inn='901234567890', responsible_full_name=user2, status='Не в работе')
