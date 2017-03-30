package com.wangc.my;

import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;
import com.typesafe.config.ConfigFactory;

/**
 * Created by wangchao on 2017/2/15.
 */
public class Test {
    public static void main(String[] args){

        ActorSystem system = ActorSystem.create("rootActor", ConfigFactory.load("xxx"));
        ActorRef a1 = system.actorOf(Props.create(Actor1.class),"actor1");
        ActorRef a2 = system.actorOf(Props.create(Actor2.class),"actor2");
        
        System.out.println( a1.path() );
        System.out.println( a2.path() );
        
        
    }
}
