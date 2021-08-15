from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        #stock = super().create(validated_data)
        print('POSITION:', positions)
        StockProduct.objects.create(**positions)


        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        print(instance, validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print('POSITION:', positions)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        StockProduct.objects.create(**positions)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
