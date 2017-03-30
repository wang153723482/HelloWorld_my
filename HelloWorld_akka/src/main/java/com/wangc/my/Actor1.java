package com.wangc.my;

import akka.actor.ActorRef;
import akka.actor.Props;
import akka.actor.UntypedActor;

/**
 * Created by wangchao on 2017/2/15.
 */
public class Actor1 extends UntypedActor {

    @Override
    public void preStart() throws Exception {
        ActorRef a1 = getContext().actorOf(Props.create(Actor2.class),"actor2_by1");
        System.out.println(a1.path());
    }

    @Override
    public void onReceive(Object message) throws Throwable {
        
    }
}
