
class RandomForestResponseForm:

    @staticmethod
    def createForm(confusionMatrix, smoteConfusionMatrix,
            y_test, y_pred, y_pred_after_smote, dataFrame):

        # smote 전 후 상관없는 공통요소
        common_info = {
            # 각 feature들과 y의 관계를 살피기 (상관 관계 분석)
            "passengers_count": dataFrame[["num_passengers", "booking_complete"]].to_dict(orient='records'),
            "purchase_lead": dataFrame[["purchase_lead", "booking_complete"]].to_dict(orient='records'),
            "length_of_stay": dataFrame[["length_of_stay", "booking_complete"]].to_dict(orient='records'),
            "extra_baggage": dataFrame[["wants_extra_baggage", "booking_complete"]].to_dict(orient='records'),
            "preferred_seat": dataFrame[["wants_preferred_seat", "booking_complete"]].to_dict(orient='records'),
            "in_flight_meals": dataFrame[["wants_in_flight_meals", "booking_complete"]].to_dict(orient='records'),
        }

        y_test_list = y_test.tolist()

        # 혼동행렬 구성
        confusionMatrixBeforeSmote = {
            'confusion_matrix':confusionMatrix.tolist(),
            'y_test':y_test_list,
            'y_pred':y_pred.tolist()
        }

        confusionMatrixAfterSmote = {
            'confusion_matrix': smoteConfusionMatrix.tolist(),
            'y_test': y_test_list,
            'y_pred': y_pred_after_smote.tolist()
        }

        return {
            'confusion_matrix_info_before_smote':confusionMatrixBeforeSmote,
            'confusion_matrix_info_after_smote':confusionMatrixAfterSmote,
            'common_info':common_info
        }