from rest_framework import serializers
from app.models import PatientRecord

YES_NO = (
    (1, "YES"),
    (0, "NO"),
)

class DiseaseParametersSerializer(serializers.Serializer):

    feature_2 = serializers.FloatField(required = True)
    feature_3 = serializers.FloatField(required = True)
    feature_4 = serializers.FloatField(required = True)
    feature_5 = serializers.FloatField(required = True)
    feature_37 = serializers.ChoiceField(required = True, choices = YES_NO)
    feature_43 = serializers.ChoiceField(required = True, choices = YES_NO)
    feature_44 = serializers.ChoiceField(required = True, choices = ((0, "0"), (2, "2"), (3, "3"), (4, "4"),
                                                                    (5, "5"), (6, "6"), (8, "8"), (9, "9")))
    def create(self, validated_data):
        return PatientRecord(**validated_data)
    
    def update(self, instance, validated_data):
        instance.feature_2 = validated_data.get('feature_2', instance.feature_2)
        instance.feature_3 = validated_data.get('feature_3', instance.feature_3)
        instance.feature_4 = validated_data.get('feature_4', instance.feature_4)
        instance.feature_5 = validated_data.get('feature_5', instance.feature_5)
        instance.feature_37 = validated_data.get('feature_37', instance.feature_37)
        instance.feature_43 = validated_data.get('feature_43', instance.feature_43)
        instance.feature_44 = validated_data.get('feature_44', instance.feature_44)
        return instance
