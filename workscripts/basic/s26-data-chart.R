# 데이터 셋 시각화
# 미국 버지니아주의 하위계층 사망율
data("VADeaths")
VADeaths

#  Rural Male Rural Female Urban Male Urban Female
# 50-54       11.7          8.7       15.4          8.4
# 55-59       18.1         11.7       24.3         13.6
# 60-64       26.9         20.3       37.0         19.3
# 65-69       41.0         30.9       54.6         35.1
# 70-74       66.0         54.3       71.1         50.0

table(VADeaths)
# beside : TRUE(그룹 막대 그래프형), FALSE(누적막대형)
barplot(VADeaths, beside=T, col = rainbow(5),
        xlab = "지역별 출신",
        ylab ="사망율",
        main="미국 버지니아주의 하위 계층 사망비율")

#범례표시
legend(20, 70, c("50~54", "55~59", "60~64", "65~69", "70~74"),
       fill = rainbow(5))
