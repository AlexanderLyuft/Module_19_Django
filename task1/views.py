from django.shortcuts import render
from task1.models import Buyer, Game

def create_records(request):
    # Вот список QuerySet запросов в порядке их вызовов, которые использованы для внесения изменений в БД
    # Создание записей Buyer
    buyer1 = Buyer.objects.create(name="Ilya", balance=1500.05, age=24)
    buyer2 = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
    buyer3 = Buyer.objects.create(name="Ubivator431", balance=0.5, age=16)

    # Создание записей Game
    game1 = Game.objects.create(title="Cyberpunk 2077", cost=31.00, size=46.2, description="Game of the year", age_limited=True)
    game2 = Game.objects.create(title="Mario", cost=5.00, size=0.5, description="Old Game", age_limited=False)
    game3 = Game.objects.create(title="Hitman", cost=12.00, size=36.6, description="Who kills Mark?", age_limited=True)

    # Связывание Buyers и Games
    game1.buyers.set([buyer1, buyer3])
    game2.buyers.set([buyer1, buyer2, buyer3])
    game3.buyers.set([buyer3])

    # Возвращаем ответ
    return render(request, 'task1/success.html', {})
