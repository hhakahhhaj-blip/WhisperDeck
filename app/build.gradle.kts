plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.fjgarcia.whisperdeck"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.fjgarcia.whisperdeck"
        minSdk = 26
        targetSdk = 34
        versionCode = 12
        versionName = "2.1.0"
    }

    buildTypes {
        release {
