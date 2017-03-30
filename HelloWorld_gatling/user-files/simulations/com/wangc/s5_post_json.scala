package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s5_post_json extends Simulation {

	val httpProtocol = http
		.baseURL("http://192.168.2.212:8080")
		.inferHtmlResources()
		.contentTypeHeader("application/json")
		.userAgentHeader("Apache-HttpClient/4.5.2 (Java/1.8.0_40)")

	val scn = scenario("reqjson")
		.exec(http("request_0")
			.post("/index_do_json.jsp")
			.body(RawFileBody("reqjson_0000_request.txt")))

	setUp(scn.inject(atOnceUsers(1))).protocols(httpProtocol)
}