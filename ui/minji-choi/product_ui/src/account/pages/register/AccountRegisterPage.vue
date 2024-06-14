<template>
    <v-container class="register-container" fill-height>
        <v-row align="center" justify="center">
            <v-col cols="12" md="8" lg="6">
                <v-card>
                    <v-card-title>
                        <span class="headline">신규 회원 신청</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form ref=form v-model="valid" lazy-validation>
                            <v-text-field
                                    v-model="email"
                                    label="Email"
                                    required
                                    :rules="emailRules"
                                    :disabled="true"/>
                            <v-row align="center">
                                <v-col cols="10">
                                    <v-text-field
                                        v-model="nickname"
                                        label="Nickname"
                                        required
                                        :rules="nicknameRules"
                                        :error-message="nicknameErrorMessages"/>
                                </v-col>
                                <v-col cols="2">
                                    <v-btn color="primary" @click="checkNicknameDuplication" class="check-button" small>
                                        중복 검사
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'

const authenticationModule = 'authenticationModule' // 왜 이렇게 하냐 ? store를 도메인 단위로 나눠서 사용하기 위함이었음
const accountModule = 'accountModule'

export default {
    data () {
        return {
            valid: false,
            email: '',
            nickname: '',
            emailRules: [
                v => !!v || 'Email은 필수입니다.', // v : vector, !! 이중 부정
                v => /.+@.+\..+/.test(v) || '유효한 Email 주소를 입력하세요.' 
                // .+ = '.' 앞에 최소 한 글자가 오고 무슨 글자가 온 다음 .이 온다
            ],
            nicknameRules: [
                v => !!v || 'Nickname은 필수입니다.'],
            nicknameErrorMessages: [],
            isNicknameValid: false,
          
        }
    },
    async created () {
        await this.requestUserInfoToDjango()
    },
    methods: {
        ...mapActions(authenticationModule, ['requestUserInfoToDjango']),
        // ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango', 'requestCreateNewAccountToDjango'])
    }
}</script>