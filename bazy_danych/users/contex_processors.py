from .models import Klient, Pracownik

def is_pracownik(request):
    """
    Dodaje do kontekstu informację, czy zalogowany użytkownik jest pracownikiem.
    """

    try:
        Klient.objects.get(login=request.user.username)
        return {'is_pracownik': False}
    except Klient.DoesNotExist:
        pass

    try:
        Pracownik.objects.get(login=request.user.username)
        return {'is_pracownik': True}
    except Pracownik.DoesNotExist:
        pass

    return {'is_pracownik': False}
    # return {
    #     'is_pracownik': getattr(request.user, 'is_pracownik', False)
    # }