FROM docker.io/library/maven:3.8.6-jdk-9-slim as builder

COPY ./pom.xml ./pom.xml
COPY ./src ./src
RUN mvn clean package

FROM docker.io/library/tomcat:8.5-jre9
COPY --from=builder /target/EShop-1.0.0.war /usr/local/tomcat/webapps/
COPY ./conf/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

EXPOSE 8080
