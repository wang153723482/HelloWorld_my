package com.wangc

import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class s6_csv extends Simulation {


	/*
	* queue 顺序调用，当csv中的数据用完即停止,但gatling会报一个错(Feeder is now empty,stopping engine.)
	* random 随机调用
	* circular 顺序循环调用
	*/

    //文件在 GATLING_HOME/user-files/data ,也可以指定绝对路径
    val csvFeeder = csv("z://foo.csv").queue

	val httpProtocol = http
		.baseURL("http://192.168.1.154:8080")
		.inferHtmlResources()
		.contentTypeHeader("application/json")

	//这里的${name}和${pwd} 是从csv中获取参数值，name和pwd是pwd的第一行
	val requestA = feed(csvFeeder).
		exec(
			http("ss")
			.post("/index_do.jsp")
			.formParam("username","${name}")
			.formParam("password","${pwd}")
		)

	val scn = scenario("scn_s6_csv")
		.exec(requestA)

	setUp(scn.inject(atOnceUsers(10))).protocols(httpProtocol)
}