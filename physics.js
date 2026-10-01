export function acceleration({mass,force,mu,v}){
 const limit=mu*mass*9.8;
 const friction=Math.abs(v)<1e-8?-Math.sign(force)*Math.min(Math.abs(force),limit):-Math.sign(v)*limit;
 return {a:(force+friction)/mass,friction,net:force+friction};
}
export function advance(state,dt){
 const {a}=acceleration(state);let {v,x}=state;
 const stopTime=a*v<0?-v/a:Infinity;
 if(stopTime<=dt){
  x+=v*stopTime+.5*a*stopTime**2;v=0;
  const rest=dt-stopTime;const next=acceleration({...state,v:0}).a;
  x+=.5*next*rest**2;v=next*rest;
 }else{x+=v*dt+.5*a*dt**2;v+=a*dt;}
 return {...state,x,v};
}
