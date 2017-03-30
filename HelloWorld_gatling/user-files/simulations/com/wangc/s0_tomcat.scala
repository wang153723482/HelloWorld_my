package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s0_tomcat extends Simulation {

	val httpProtocol = http
		.baseURL("http://192.168.2.212:8080")
		.inferHtmlResources()

	val scn = scenario("HelloWorld").during(2){
		exec(http("request_0")
			.get("/index_do.jsp?username=aaaaaaa")
			.resources())
        }

	setUp(scn.inject(atOnceUsers(5))).protocols(httpProtocol)
}
