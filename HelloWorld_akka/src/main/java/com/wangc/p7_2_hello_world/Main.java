package com.wangc.p7_2_hello_world;

import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;
import com.typesafe.config.ConfigFactory;
import com.wangc.Msg;
import com.wangc.p7_2_hello_world.Greeter;
import com.wangc.p7_2_hello_world.HelloWorld;

/**
 * Created by wangchao on 2017/1/22.
 */
public class Main {
    public static void main(String[] args) {
        //管理和维护Actor的系统，一般一个系统创建一个即可
        ActorSystem system = ActorSystem.create("HelloAkka", ConfigFactory.load("samplehello.conf"));

        //通过 ActorSystem 创建一个 【顶级】 actor
        ActorRef helloWorld = system.actorOf(Props.create(HelloWorld.class), "helloWorldActor");

        //通过 ActorSystem 创建一个 【顶级】 actor
        ActorRef greeter = system.actorOf(Props.create(Greeter.class), "greeterActor");

        greeter.tell(Msg.HELLO, helloWorld); //greeter 是接收者，第二个参数是sender（发送者）

        System.out.println("Main===HelloWorld Actor Path: " + helloWorld.path());
        System.out.println("Main===Greeter Actor Path: " + greeter.path());
    }
}
