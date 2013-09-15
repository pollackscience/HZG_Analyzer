      double complex function Fvs(st,j1,j2,j3,j4,j5,j6,za,zb) 
      implicit none
      integer j1,j2,j3,j4,j5,j6
      include 'constants.f'
      include 'zprods_decl.f'
      include 'sprods_com.f'
      character*9 st
      double complex L0,L1,Lsm1_2mh,Lsm1_2me,I3m,Lnrat
      double precision t  
      if(st.eq.'q+qb-g+g-') then
      Fvs= 
     .((za(j2,j5)*zb(j1,j2)+za(j3,j5)*zb(j1,j3))**2-
     .za(j2,j5)*za(j5,j6)*zb(j1,j2)*zb(j1,j6))/
     .(za(j5,j6)*zb(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))*
     .*2)+
     .(za(j2,j5)*((-s(j1,j2)+s(j3,j4)-s(j5,j6))*za(j2,j5)-
     .2d0*za(j1,j2)*za(j5,j6)*zb(j1,j6))*
     .(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*za(j1,j2)*za(j5,j6)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .(2d0*za(j1,j2)*za(j4,j5)*zb(j1,j4)*
     .(-((L0(-t(j1,j2,j4),-s(j1,j2))/s(j1,j2)-
     .L1(-t(j1,j2,j4),-s(j1,j2))/(2d0*s(j1,j2)))*za(j4,j5)*zb(j1,j4))+
     .(L0(-t(j1,j2,j4),-s(j1,j2))*
     .(za(j2,j3)*zb(j1,j2)-za(j3,j4)*zb(j1,j4))*
     .(-(za(j1,j5)*zb(j1,j4))-za(j2,j5)*zb(j2,j4)))/
     .(s(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))))/
     .(za(j5,j6)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2)+
     .(2d0*za(j2,j3)*zb(j1,j2)*zb(j3,j6)*
     .((L0(-t(j1,j2,j3),-s(j1,j2))*
     .(-(za(j1,j3)*zb(j1,j6))-za(j2,j3)*zb(j2,j6))*
     .(-(za(j1,j2)*zb(j1,j4))+za(j2,j3)*zb(j3,j4)))/
     .(s(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))-
     .(L0(-t(j1,j2,j3),-s(j1,j2))/s(j1,j2)-
     .L1(-t(j1,j2,j3),-s(j1,j2))/(2d0*s(j1,j2)))*za(j2,j3)*zb(j3,j6)))/
     .((-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2*zb(j5,j6))
     
      Fvs=Fvs+
     .(2d0*za(j3,j5)*zb(j1,j3)*(-((L0(-t(j3,j5,j6),-s(j5,j6))/s(j5,j6)-
     .L1(-t(j3,j5,j6),-s(j5,j6))/(2d0*s(j5,j6)))*za(j3,j5)*zb(j1,j3))+
     .(L0(-t(j3,j5,j6),-s(j5,j6))*
     .(-(za(j3,j5)*zb(j1,j5))-za(j3,j6)*zb(j1,j6))*
     .(-(za(j3,j5)*zb(j3,j4))-za(j5,j6)*zb(j4,j6)))/
     .(s(j5,j6)*(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))))*zb(j5,j6)
     .)/(zb(j1,j2)*(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**2)+
     .(zb(j1,j6)*(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .((-s(j1,j2)+s(j3,j4)-s(j5,j6))*zb(j1,j6)-
     .2d0*za(j2,j5)*zb(j1,j2)*zb(j5,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*zb(j1,j2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))*zb(j5,j6))+
     .((-(za(j1,j2)*zb(j1,j6))+za(j2,j4)*zb(j4,j6))**2-
     .za(j1,j2)*za(j2,j5)*zb(j1,j6)*zb(j5,j6))/
     .(za(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2*zb(j5,j
     .6))+
     .(2d0*za(j2,j4)*za(j5,j6)*zb(j4,j6)*
     .(-((L0(-t(j4,j5,j6),-s(j5,j6))/s(j5,j6)-
     .L1(-t(j4,j5,j6),-s(j5,j6))/(2d0*s(j5,j6)))*za(j2,j4)*zb(j4,j6))+
     .(L0(-t(j4,j5,j6),-s(j5,j6))*
     .(-(za(j2,j5)*zb(j4,j5))-za(j2,j6)*zb(j4,j6))*
     .(za(j3,j4)*zb(j4,j6)+za(j3,j5)*zb(j5,j6)))/
     .(s(j5,j6)*(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6)))))/
     .(za(j1,j2)*(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**2)-
     .(2d0*Lsm1_2mh(s(j3,j4),t(j1,j2,j3),s(j1,j2),s(j5,j6))*za(j2,j3)*
     .(-(za(j1,j3)*zb(j1,j6))-za(j2,j3)*zb(j2,j6))*zb(j4,j6)*
     .(-(za(j2,j5)*zb(j4,j5))-za(j2,j6)*zb(j4,j6))*t(j1,j2,j3))/
     .(za(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**4*zb(j5,j
     .6))
     
      Fvs=Fvs+
     .Lnrat(-t(j1,j2,j3),-s(j3,j4))*(-((2d0*za(j2,j3)*za(j2,j4)*zb(j3,j6
     .)*zb(j4,j6)+
     .(-(za(j1,j2)*zb(j1,j6))+za(j2,j4)*zb(j4,j6))**2)/
     .(za(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2*
     .zb(j5,j6)))+(2d0*za(j2,j3)*zb(j4,j6)*
     .(-(za(j1,j2)*zb(j1,j6))+za(j2,j4)*zb(j4,j6))*t(j1,j2,j3))/
     .(za(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**3*zb(j5,j
     .6))
     .)+I3m(s(j1,j2),s(j3,j4),s(j5,j6))*
     .(-((za(j2,j4)*za(j4,j5)*zb(j1,j3)*zb(j3,j6))/
     .(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,j
     .6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2))-
     .(za(j2,j3)*za(j3,j5)*zb(j1,j4)*
     .(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))**2*zb(j4,j6))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2)-
     .(3d0*(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .(-(za(j2,j4)*za(j3,j5)*zb(j1,j4)*zb(j3,j6))-
     .za(j2,j3)*za(j4,j5)*zb(j1,j3)*zb(j4,j6)+
     .(s(j3,j4)*(-s(j1,j2)+s(j3,j4)-s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-
     .2d0*s(j1,j2)*s(j5,j6)-2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .(2d0*za(j2,j3)*(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*zb(j4,
     .j6)*
     .(-((za(j2,j5)*zb(j1,j2)+za(j4,j5)*zb(j1,j4))*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .za(j2,j3)*za(j5,j6)*zb(j1,j2)*zb(j4,j6))*
     .(t(j1,j2,j3)-t(j1,j2,j4)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**3))
     
      Fvs=Fvs-
     .Lnrat(-s(j1,j2),-s(j3,j4))*((3d0*(-s(j1,j2)-s(j3,j4)+s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)**2*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .((-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .((za(j2,j5)**2*zb(j1,j2))/za(j5,j6)-2d0*za(j2,j5)*zb(j1,j6)+
     .(za(j1,j2)*zb(j1,j6)**2)/zb(j5,j6)))/
     .(2d0*(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s
     .(j5,j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))-
     .(za(j2,j5)*zb(j1,j2)*(((s(j1,j2)-s(j3,j4)-s(j5,j6))*
     .(za(j1,j2)*za(j5,j6)*zb(j1,j6)+za(j2,j5)*t(j1,j2,j3)))/
     .za(j5,j6)+2d0*za(j2,j3)*zb(j3,j6)*(t(j1,j2,j3)-t(j1,j2,j4))))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2)+
     .(2d0*za(j2,j3)*zb(j1,j2)*zb(j4,j6)*
     .(za(j1,j2)*za(j5,j6)*zb(j1,j6)+za(j2,j5)*t(j1,j2,j3))*
     .(t(j1,j2,j3)-t(j1,j2,j4)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**3))-
     .(2d0*Lsm1_2mh(s(j3,j4),t(j1,j2,j4),s(j1,j2),s(j5,j6))*za(j3,j5)*zb
     .(j1,j4)*
     .(-(za(j3,j5)*zb(j1,j5))-za(j3,j6)*zb(j1,j6))*
     .(-(za(j1,j5)*zb(j1,j4))-za(j2,j5)*zb(j2,j4))*t(j1,j2,j4))/
     .(za(j5,j6)*zb(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))*
     .*4)+
     .Lnrat(-t(j1,j2,j4),-s(j3,j4))*(-(((za(j2,j5)*zb(j1,j2)+za(j3,j5)*z
     .b(j1,j3))**
     .2+2d0*za(j3,j5)*za(j4,j5)*zb(j1,j3)*zb(j1,j4))/
     .(za(j5,j6)*zb(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-
     .za(j2,j3)*zb(j2,j4))**2))+
     .(2d0*za(j3,j5)*(za(j2,j5)*zb(j1,j2)+za(j3,j5)*zb(j1,j3))*zb(j1,j4)
     .*
     .t(j1,j2,j4))/
     .(za(j5,j6)*zb(j1,j2)*(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))*
     .*3)
     .)
     
      Fvs=Fvs+
     .I3m(s(j1,j2),s(j3,j4),s(j5,j6))*
     .(-((za(j2,j4)*za(j4,j5)*zb(j1,j3)*zb(j3,j6))/
     .(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,j
     .6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2))-
     .(za(j2,j3)*za(j3,j5)*zb(j1,j4)*
     .(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))**2*zb(j4,j6))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2)-
     .(3d0*(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .(-(za(j2,j4)*za(j3,j5)*zb(j1,j4)*zb(j3,j6))-
     .za(j2,j3)*za(j4,j5)*zb(j1,j3)*zb(j4,j6)+
     .(s(j3,j4)*(-s(j1,j2)+s(j3,j4)-s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-
     .2d0*s(j1,j2)*s(j5,j6)-2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .(2d0*za(j3,j5)*zb(j1,j4)*(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j
     .3))*
     .(-((-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))*
     .(-(za(j1,j2)*zb(j1,j6))+za(j2,j3)*zb(j3,j6)))+
     .za(j1,j2)*za(j3,j5)*zb(j1,j4)*zb(j5,j6))*
     .(-t(j1,j2,j3)+t(j1,j2,j4)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**3))
     
      Fvs=Fvs-
     .Lnrat(-s(j1,j2),-s(j3,j4))*((3d0*(-s(j1,j2)-s(j3,j4)+s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)**2*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))+
     .((-(za(j1,j4)*zb(j1,j3))-za(j2,j4)*zb(j2,j3))*
     .((za(j2,j5)**2*zb(j1,j2))/za(j5,j6)-2d0*za(j2,j5)*zb(j1,j6)+
     .(za(j1,j2)*zb(j1,j6)**2)/zb(j5,j6)))/
     .(2d0*(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s
     .(j5,j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4)))-
     .(2d0*za(j1,j2)*za(j3,j5)*zb(j1,j4)*(-t(j1,j2,j3)+t(j1,j2,j4))*
     .(za(j2,j5)*zb(j1,j2)*zb(j5,j6)+zb(j1,j6)*t(j1,j2,j4)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**3)+
     .(za(j1,j2)*zb(j1,j6)*(2d0*za(j4,j5)*zb(j1,j4)*
     .(-t(j1,j2,j3)+t(j1,j2,j4))-
     .((s(j1,j2)-s(j3,j4)-s(j5,j6))*
     .(za(j2,j5)*zb(j1,j2)*zb(j5,j6)+zb(j1,j6)*t(j1,j2,j4)))/
     .zb(j5,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j1,j3)*zb(j1,j4))-za(j2,j3)*zb(j2,j4))**2))
     
      Fvs=Fvs-
     .Lnrat(-s(j5,j6),-s(j3,j4))*((3d0*(s(j1,j2)-s(j3,j4)-s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j4,j5)*zb(j3,j5))-za(j4,j6)*zb(j3,j6))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)**2*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6)))+
     .((-(za(j4,j5)*zb(j3,j5))-za(j4,j6)*zb(j3,j6))*
     .(-2d0*za(j2,j5)*zb(j1,j6)+(za(j5,j6)*zb(j1,j6)**2)/zb(j1,j2)+
     .(za(j2,j5)**2*zb(j5,j6))/za(j1,j2)))/
     .(2d0*(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s
     .(j5,j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6)))-
     .(za(j2,j5)*zb(j5,j6)*(-(((-s(j1,j2)-s(j3,j4)+s(j5,j6))*
     .(-(za(j1,j2)*za(j5,j6)*zb(j1,j6))-za(j2,j5)*t(j3,j5,j6))
     .)/za(j1,j2))+2d0*za(j3,j5)*zb(j1,j3)*(t(j3,j5,j6)-t(j4,j5,j6))))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**2)-
     .(2d0*za(j3,j5)*zb(j1,j4)*zb(j5,j6)*
     .(-(za(j1,j2)*za(j5,j6)*zb(j1,j6))-za(j2,j5)*t(j3,j5,j6))*
     .(t(j3,j5,j6)-t(j4,j5,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**3))
     
      Fvs=Fvs-
     .Lnrat(-s(j5,j6),-s(j3,j4))*((3d0*(s(j1,j2)-s(j3,j4)-s(j5,j6))*
     .(-(za(j2,j3)*zb(j1,j3))-za(j2,j4)*zb(j1,j4))*
     .(-(za(j4,j5)*zb(j3,j5))-za(j4,j6)*zb(j3,j6))*
     .(-(za(j3,j5)*zb(j3,j6))-za(j4,j5)*zb(j4,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)**2*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6)))+
     .((-(za(j4,j5)*zb(j3,j5))-za(j4,j6)*zb(j3,j6))*
     .(-2d0*za(j2,j5)*zb(j1,j6)+(za(j5,j6)*zb(j1,j6)**2)/zb(j1,j2)+
     .(za(j2,j5)**2*zb(j5,j6))/za(j1,j2)))/
     .(2d0*(s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s
     .(j5,j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6)))+
     .(2d0*za(j2,j3)*za(j5,j6)*zb(j4,j6)*(-t(j3,j5,j6)+t(j4,j5,j6))*
     .(-(za(j2,j5)*zb(j1,j2)*zb(j5,j6))-zb(j1,j6)*t(j4,j5,j6)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**3)+
     .(za(j5,j6)*zb(j1,j6)*(2d0*za(j2,j4)*zb(j4,j6)*
     .(-t(j3,j5,j6)+t(j4,j5,j6))+
     .((-s(j1,j2)-s(j3,j4)+s(j5,j6))*
     .(-(za(j2,j5)*zb(j1,j2)*zb(j5,j6))-zb(j1,j6)*t(j4,j5,j6)))/
     .zb(j1,j2)))/
     .((s(j1,j2)**2-2d0*s(j1,j2)*s(j3,j4)+s(j3,j4)**2-2d0*s(j1,j2)*s(j5,
     .j6)-
     .2d0*s(j3,j4)*s(j5,j6)+s(j5,j6)**2)*
     .(-(za(j3,j5)*zb(j4,j5))-za(j3,j6)*zb(j4,j6))**2))
      elseif(st.eq.'q+qb-g+g+') then
      Fvs= 
     .-((Lsm1_2me(t(j1,j2,j3),t(j1,j2,j4),s(j1,j2),s(j5,j6))*za(j2,j3)*z
     .a(j2,j4)*
     .za(j3,j5)*za(j4,j5))/(za(j1,j2)*za(j3,j4)**4*za(j5,j6)))-
     .(Lsm1_2me(t(j1,j2,j4),t(j1,j2,j3),s(j1,j2),s(j5,j6))*za(j2,j3)*za(
     .j2,j4)*
     .za(j3,j5)*za(j4,j5))/(za(j1,j2)*za(j3,j4)**4*za(j5,j6))+
     .(L0(-t(j1,j2,j3),-s(j1,j2))*za(j2,j5)*za(j3,j5)*zb(j1,j3))/
     .(s(j1,j2)*za(j3,j4)**2*za(j5,j6))-
     .(L1(-t(j1,j2,j3),-s(j1,j2))*za(j1,j2)*za(j3,j5)**2*zb(j1,j3)**2)/
     .(s(j1,j2)**2*za(j3,j4)**2*za(j5,j6))+
     .(L0(-t(j1,j2,j4),-s(j1,j2))*za(j2,j5)*za(j4,j5)*zb(j1,j4))/
     .(s(j1,j2)*za(j3,j4)**2*za(j5,j6))-
     .(L1(-t(j1,j2,j4),-s(j1,j2))*za(j1,j2)*za(j4,j5)**2*zb(j1,j4)**2)/
     .(s(j1,j2)**2*za(j3,j4)**2*za(j5,j6))+
     .(L0(-t(j3,j5,j6),-s(j5,j6))*za(j2,j3)*za(j2,j5)*zb(j3,j6))/
     .(s(j5,j6)*za(j1,j2)*za(j3,j4)**2)-
     .(L1(-t(j3,j5,j6),-s(j5,j6))*za(j2,j3)**2*za(j5,j6)*zb(j3,j6)**2)/
     .(s(j5,j6)**2*za(j1,j2)*za(j3,j4)**2)+
     .((za(j2,j4)*za(j3,j5)+za(j2,j3)*za(j4,j5))*
     .(-(Lnrat(-t(j1,j2,j4),-t(j1,j2,j3))*za(j2,j5))/2d0+
     .(L0(-t(j1,j2,j4),-s(j1,j2))*za(j1,j2)*za(j4,j5)*zb(j1,j4))/s(j1,j2
     .)+
     .(L0(-t(j1,j2,j4),-s(j5,j6))*za(j2,j3)*za(j5,j6)*zb(j3,j6))/s(j5,j6
     .)))/
     .(za(j1,j2)*za(j3,j4)**3*za(j5,j6))+
     .(L0(-t(j4,j5,j6),-s(j5,j6))*za(j2,j4)*za(j2,j5)*zb(j4,j6))/
     .(s(j5,j6)*za(j1,j2)*za(j3,j4)**2)-
     .(L1(-t(j4,j5,j6),-s(j5,j6))*za(j2,j4)**2*za(j5,j6)*zb(j4,j6)**2)/
     .(s(j5,j6)**2*za(j1,j2)*za(j3,j4)**2)-
     .((za(j2,j4)*za(j3,j5)+za(j2,j3)*za(j4,j5))*
     .(-(Lnrat(-t(j1,j2,j3),-t(j1,j2,j4))*za(j2,j5))/2d0+
     .(L0(-t(j1,j2,j3),-s(j1,j2))*za(j1,j2)*za(j3,j5)*zb(j1,j3))/s(j1,j2
     .)+
     .(L0(-t(j1,j2,j3),-s(j5,j6))*za(j2,j4)*za(j5,j6)*zb(j4,j6))/s(j5,j6
     .)))/
     .(za(j1,j2)*za(j3,j4)**3*za(j5,j6))+
     .(za(j2,j5)**2/(za(j1,j2)*za(j5,j6))-zb(j1,j6)**2/(zb(j1,j2)*zb(j5,
     .j6)))/
     .za(j3,j4)**2
      endif
      return
      end