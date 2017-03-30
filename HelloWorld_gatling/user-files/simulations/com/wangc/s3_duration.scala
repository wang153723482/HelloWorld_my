package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s3_duration extends Simulation {

	val httpProtocol = http
		.baseURL("http://192.168.2.212:8080")
		.inferHtmlResources()

//setting the time of running,default is second,and you can use millisecond too.
//during(10) or during(10000 milliseconde) 
	val scn = scenario("HelloWorld").during(2){
			exec(http("request_0")
			.get("/index_do.jsp?username=aaaaaaa")
			.resources())
        }

	setUp(scn.inject(atOnceUsers(5))).protocols(httpProtocol)
}