FROM openjdk:21
COPY target/stateful-any-api-0.0.1-SNAPSHOT.jar app.jar
EXPOSE  8083
ENTRYPOINT ["java", "-jar", "app.jar"]