package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s2_rampup extends Simulation {

	val httpProtocol = http
		.baseURL("http://192.168.2.212:8080")
		.inferHtmlResources()

	val scn = scenario("HelloWorld")
			.exec(http("request_0")
			.get("/index_do.jsp?username=aaaaaaa")
			.resources())

//rampUsers(5) over(10) use 10 secends start 5 vu
	setUp(scn.inject(rampUsers(5) over(10))).protocols(httpProtocol)
}