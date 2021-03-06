export default {
  name: 'ContactUsComponent',
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    waiting: false,
    valid: false,
    vs: {
      v1: false,
      v2: false,
      v3: false
    },
    forums_icon: '',
    fullname: '',
    email: '',
    message: ''
  }),
  computed: {
    i18n() { return this.$store.state.i18n.contact },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    chackValid() {
      let root = this

      root.vs.v1 = true
      root.vs.v2 = true
      root.vs.v3 = true

      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = false } })
      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = false } })
      root.meRules.forEach((rule) => { if (rule(root.message) !== true) { root.vs.v3 = false } })

      root.valid = root.vs.v1 && root.vs.v2 && root.vs.v3
    },
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        root.waiting = await this.$auth.contact(root)
      }
    }
  },
  created() {
    if (this.$store.getters.isLogin) {
      this.fullname = this.$store.getters.user('name')
      this.email = this.$store.getters.user('email')
    }

    this.fnRules = [
      v => !!v || '',
      v => (v && v.length <= 20) || this.form.fullname_length_error
    ]
    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.form.email_validator_error
    ]
    this.meRules = [
      v => !!v || '',
      v => (v && v.length >= 10) || this.form.message_length_error
    ]

    this.$store.dispatch('getImgUrl', 'icons/forums-logo.png').then(img => {
      this.forums_icon = img
    }).catch(error => {
      throw new Error(error.message)
    })
  },
  updated() {
    this.chackValid()
  }
}
