

class Basket():
    """
    Базовый класс корзины, предоставляющий некоторые параметры поведения по умолчанию, которые
    при необходимости могут быть унаследованы или переопределены.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket
