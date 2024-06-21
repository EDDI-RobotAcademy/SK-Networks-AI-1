class RandomForestResponseForm:
    @staticmethod
    def createForm(confusionMatrix, smoteConfusionMatrix,
                   y_test, y_pred, y_pred_after_smote, data):

        # 공통 정보
        common_info = {
            "passengers_count": data[['num_passengers', 'booking_complete']].to_dict(orient='records'),
            "purchase_lead": data[['purchase_lead', 'booking_complete']].to_dict(orient='records'),
            "length_of_stay": data[['length_of_stay', 'booking_complete']].to_dict(orient='records'),
            "extra_baggage": data[['wants_extra_baggage', 'booking_complete']].to_dict(orient='records'),
            "preferred_seat": data[['wants_preferred_seat', 'booking_complete']].to_dict(orient='records'),
            "in_flight_meals": data[['wants_in_flight_meals', 'booking_complete']].to_dict(orient='records'),
        }

        y_test_list = y_test.tolist()

        # 혼동 행렬 구성
        confusionMatrixBeforeSmote = {
            'confusion_matrix_before_smote': confusionMatrix.tolist(),
            'y_test': y_test_list,
            'y_pred_before_smote': y_pred.tolist()
        }

        confusionMatrixAfterSmote = {
            'confusion_matrix_after_smote': smoteConfusionMatrix.tolist(),
            'y_test': y_test_list,
            'y_pred_after_smote': y_pred_after_smote.tolist()
        }

        return {
            'confusion_matrix_info_before_smote': confusionMatrixBeforeSmote,
            'confusion_matrix_info_after_smote': confusionMatrixAfterSmote,
            'common_info': common_info
        }
