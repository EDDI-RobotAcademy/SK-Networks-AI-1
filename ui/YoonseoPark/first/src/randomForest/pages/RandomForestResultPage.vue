<template>
    <v-container v-if="confusionMatrixInfoBeforeSmote && confusionMatrixInfoAfterSmote">
        <v-row>
            <v-col cols="6">
                <v-card>
                    <v-card-titile class="headline">
                        Confusion Matrix before SMOTE    
                    </v-card-titile>
                    <v-card-text>
                        <confusion-matrix :confusionMatrix="confusionMatrixInfoBeforeSmote.confusion_matrix"/>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card>
                    <v-card-titile class="headline">
                        Confusion Matrix after SMOTE    
                    </v-card-titile>
                    <v-card-text>
                        <confusion-matrix :confusionMatrix="confusionMatrixInfoAfterSmote.confusion_matrix"/>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    data () {
        return {
            confusionMatrixInfoBeforeSmote: null,
            confusionMatrixInfoAfterSmote: null,
            passengersCountInfo: [],
            purchaseLeadInfo: [],
            lengthOfStayInfo: [],
            extraBaggageInfo: [],
            preferredSeatInfo: [],
            inFlightMealsInfo: [],
        }
    },
    mounted() {
        this.fetchFlilghtDataOnRandomForestAnalysis()
    },
    methods: {
        async fetchFlilghtDataOnRandomForestAnalysis () {
            const response = await fetch('http://localhost:33333/random-forest')
            const data = await response.json()

            console.log('data: ', data)

            this.confusionMatrixInfoBeforeSmote = data.confusion_matrix_info_before_smote
            this.confusionMatrixInfoAfterSmote = data.confusion_matrix_info_after_smote
        }
    },
}

</script>

