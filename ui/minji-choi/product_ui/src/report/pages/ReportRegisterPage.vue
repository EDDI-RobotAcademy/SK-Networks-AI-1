<template>
    <v-container>
      <v-card class="mx-auto my-12" max-width="600">
        <v-card-title>
          <span class="headline">회원 가입 설문조사</span>
        </v-card-title>
        <v-card-subtitle>
          <span>신규 회원님, 환영합니다!<br> 더 나은 상품 추천을 위해 추가적인 정보를 요청합니다. <br>아래 설문을 작성해 주세요.</span>
        </v-card-subtitle>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="age"
                  label="나이를 입력하세요. * 숫자로 입력"
                  required
                  :rules="ageRules"
                  type="number"
                  outlined
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="gender"
                  :items="gender_select"
                  label="성별을 선택하세요."
                  clearable
                  solo
                  outlined
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="text-right">
                <v-btn
                  class="ml-2"
                  color="primary"
                  @click="onSubmit"
                  :disabled="!valid"
                >
                  <v-icon left>mdi-check</v-icon>
                  작성 완료
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  const reportModule = 'reportModule'
  
  export default {
    data() {
      return {
        age: '',
        gender: '',
        gender_select: ['여성', '남성'],
        valid: false,
        ageRules: [
          v => !!v || '나이는 필수 입력 항목입니다.',
          v => (v && v > 0) || '유효한 나이를 입력하세요.'
        ]
      }
    },
    methods: {
      ...mapActions(reportModule, ['requestCreateReportToDjango']),
      async onSubmit() {
        if (this.$refs.form.validate()) {
          const payload = {
            age: this.age,
            gender: this.gender
          }
  
          try {
            const report = await this.requestCreateReportToDjango(payload)
            alert('작성이 완료되었습니다.')
            await this.$router.push('/')
          } catch (error) {
            console.error('Error submitting the form:', error)
            alert('설문 작성 중 오류가 발생했습니다. 다시 시도해 주세요.')
          }
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .headline {
    font-weight: bold;
  }
  </style>
  