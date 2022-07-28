from rest_framework import serializers  #belli bir formata sokuyor
from api.models import Makale

class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True) 
    yazar = serializers.CharField()  
    baslik = serializers.CharField(max_length=120)
    aciklama = serializers.CharField(max_length=200)
    metin = serializers.TextField() #text istiyor
    sehir = serializers.BooleanField(default=True) #boolean değer
    yayımlanma_tarihi = serializers.DateField()
    aktif =  serializers.BooleanField(default=True)
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    güncelleme_tarihi = serializers.DateTimeField(read_only=True) 

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data): #bir obje göndeiliyor 
    instance.yazar = validated_data.get('yazar', instance.yazar)  #update edilecek bir alan var mı yazarın karşısında bir değer varsa al yoksa instance içindekini kullan değişiklik olmamış
    instance.baslik = validated_data.get('baaslik', instance.baslik)
    instance.aciklama = validated_data.get('aciklama', instance.aciklama)
    instance.metin = validated_data.get('metin', instance.metin) 
    instance.sehir = validated_data.get('sehir', instance.sehir) #boolean değer
    instance.yayımlanma_tarihi = validated_data.get('yayımlanma_tarihi', instance.yayımlanma_tarihi)
    instance.aktif =  validated_data.get('aktif', instance.aktif)
    instance.save()
    return instance 
