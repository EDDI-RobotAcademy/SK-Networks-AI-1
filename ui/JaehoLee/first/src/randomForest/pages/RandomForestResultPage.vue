<template>
    <v-container v-if="confusionMatrixInfoBeforeSmote && confusionMatrixInfoAfterSmote">
        <v-row>
            <v-col cols="6">
                <v-card>
                    <v-card-title class="headline">
                        Confusion Matrix before SMOTE
                    </v-card-title>
                    <v-card-text>
                        <confusion-matrix 
                        :confusionMatrix="confusionMatrixInfoBeforeSmote.confusion_matrix"/>
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="6">
                <v-card>
                    <v-card-title class="headline">
                        Confusion Matrix after SMOTE
                    </v-card-title>
                    <v-card-text>
                        <confusion-matrix 
                        :confusionMatrix="confusionMatrixInfoAfterSmote.confusion_matrix"/>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <!-- 그래프 플로팅 -->
        <v-row>
            <v-col cols="6">
                <common-chart
                    :title="`Passengers number vs Booking Complete`"
                    :data="passengersCounterInfo"
                    graphType="countplot"
                    xKey="num_passengers"
                    hueKey="booking_complete"/>
            </v-col>
            <v-col cols="6">
                <common-chart
                    :title="`Purchase Lead vs Booking Complete`"
                    :data="purchaseLeadInfo"
                    graphType="histplot"
                    xKey="purchase_lead"
                    hueKey="booking_complete"
                    bins="30"/>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="6">
                <common-chart
                    :title="`Length of Stay vs Booking Complete`"
                    :data="lengthOfStayInfo"
                    graphType="histplot"
                    xKey="length_of_stay"
                    hueKey="booking_complete"
                    bins="30"/>
            </v-col>
            <v-col cols="6">
                <common-chart
                    :title="`Wants Extra Baggage vs Booking Complete`"
                    :data="extraBaggageInfo"
                    graphType="countplot"
                    xKey="wants_extra_baggage"
                    hueKey="booking_complete"/>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="6">
                <common-chart
                    :title="`Wants Preferred Seat vs Booking Complete`"
                    :data="preferredSeatInfo"
                    graphType="countplot"
                    xKey="wants_preferred_seat"
                    hueKey="booking_complete"/>
            </v-col>
            <v-col cols="6">
                <common-chart
                    :title="`Wants In-Flight Meals vs Booking Complete`"
                    :data="inFlightMealsInfo"
                    graphType="countplot"
                    xKey="wants_in_flight_meals"
                    hueKey="booking_complete"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import ConfusionMatrix from '@/randomForest/components/ConfusionMatrix.vue'
import CommonChart from '@/randomForest/components/CommonChart.vue'
import axiosInstance from '@/utility/axiosInstance'

export default {
    components: {
        ConfusionMatrix,
        CommonChart,
    },
    data () {
        return {
            confusionMatrixInfoBeforeSmote: null,
            confusionMatrixInfoAfterSmote: null,
            passengersCounterInfo: [],
            purchaseLeadInfo: [],
            lengthOfStayInfo: [],
            extraBaggageInfo: [],
            preferredSeatInfo: [],
            inFlightMealsInfo: [],
        }
    },
    mounted () {
        this.fetchFlightDataOnRandomForestAnalysis()
    },
    methods: {
        async fetchFlightDataOnRandomForestAnalysis () {
            const response = await fetch('http://192.168.0.18:33333/random-forest')
            const data = await response.json()
            // const response = await axiosInstance.fastapiAxiosInst.fetch('/random-forest')
            // const data = response.data

            console.log('data:', data)

            this.confusionMatrixInfoBeforeSmote = data.confusion_matrix_info_before_smote
            this.confusionMatrixInfoAfterSmote = data.confusion_matrix_info_after_smote

            this.passengersCounterInfo = data.common_info.passengers_count
            this.purchaseLeadInfo = data.common_info.purchase_lead
            this.lengthOfStayInfo = data.common_info.length_of_stay
            this.extraBaggageInfo = data.common_info.extra_baggage
            this.preferredSeatInfo = data.common_info.preferred_seat
            this.inFlightMealsInfo = data.common_info.in_flight_meals
        }
    }
}
</script>