package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s4_post_form extends Simulation {

	val httpProtocol = http
		.baseURL("http://localhost:8080")

	val scn = scenario("post")
		.exec(http("request_0")
			.post("/index_do.jsp")
			.formParam("username", "wangchao11")
			.formParam("password", "123111")
			)

	setUp(scn.inject(atOnceUsers(1))).protocols(httpProtocol)
}