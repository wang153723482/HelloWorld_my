package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s5_post_json2 extends Simulation {

	val httpProtocol = http
		.baseURL("http://192.168.103.154:8080")
		.inferHtmlResources()
		.contentTypeHeader("application/json")

	val scn = scenario("s5_req_json2")
		.exec(http("request_0")
			.post("/index_do_json.jsp")
			.body(StringBody("{\"name\":\"wangc\"}")))

	setUp(scn.inject(atOnceUsers(1))).protocols(httpProtocol)
}