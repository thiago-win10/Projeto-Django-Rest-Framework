from rest_framework import serializers

from .models import Curso, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')


    def validate_avaliacao(self, valor):
        if valor <= 5:
            return valor
        else:
            raise serializers.ValidationError("A avaliação precisa ser um inteiro entre 1 e 5")


class CursoSerializer(serializers.ModelSerializer):
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    #avaliacoes = serializers.StringRelatedField(many=True, read_only=True)
    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #avaliacoes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nome')
    avaliacoes = serializers.HyperlinkedIdentityField(view_name='avaliacao-detail', lookup_field='pk')

    media_avaliacoes = serializers.SerializerMethodField()



    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media * 2) / 2

