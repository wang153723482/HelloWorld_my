package com.wangc.p7_4_life_cycle;

import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.PoisonPill;
import akka.actor.Props;
import com.typesafe.config.ConfigFactory;

/**
 * Created by wangchao on 2017/2/15.
 */
public class DeadMain {
    public static void main(String[] args){

        ActorSystem system = ActorSystem.create("deadwatch", ConfigFactory.load("samplehello.conf"));
        ActorRef work = system.actorOf(Props.create(MyWorker.class),"worker");
        system.actorOf(Props.create(WatchActor.class,work),"watcher");
        
        work.tell(MyWorker.Msg.WORKING,ActorRef.noSender());
        work.tell(MyWorker.Msg.DONE,ActorRef.noSender());
        work.tell(PoisonPill.getInstance(),ActorRef.noSender());//PoisonPill 毒药，给work发了一个毒药。
        
        
    }
}
