%%%%
%%  LILLIPUT_lib.m
%%%%

%%%%
%% Creation du state
%%%%

function state=create_state(X, m)
%% Transform a message X (binaire -> m=0, hexadecimal -> m=1) to a state to be processed
  state=[];
  if m<=0
    for i=1:4:(length(X)-3)
      state=[bin2dec(X(i:i+3)) state];
    end
  else
    for i=1:length(X)
      state(length(X)-(i-1))=hex2dec(X(i));
    end
end

%%%%
%% Round function
%%%%

function state=nonlinear_layer(X,K,sbox)
  for i=1:8
    s=sbox(bitxor(X(9-i), K(i))+1);
    X(8+i)=bitxor(X(8+i), sbox(bitxor(X(9-i), K(i))+1));
  end
  state=X;
end

function state=linear_layer(X)
  for i=2:7
    X(16)=bitxor(X(16),X(i));
    X(17-i)=bitxor(X(17-i),X(8));
  end
  X(16)=bitxor(X(16),X(8));
  state=X;
end

function state=permutation(X, perm)
  for i=1:16
    state(perm(i)+1)=X(i);
  end
end

%%%%
%%  Keyschedule
%%%%

function RK=exctract_round_key(K, i, sbox)
  tmp=[dec2bin(K(19),4) dec2bin(K(17),4) dec2bin(K(14),4) dec2bin(K(11),4) dec2bin(K(10),4) dec2bin(K(7),4) dec2bin(K(4),4) dec2bin(K(2),4)];
  RK='';
  for j=1:8
    s=bin2dec([tmp(j) tmp(8+j) tmp(16+j) tmp(24+j)]);
    RK_tmp(j)=sbox(1+bin2dec([tmp(j) tmp(8+j) tmp(16+j) tmp(24+j)]));
    RK=[RK dec2bin(RK_tmp(j),4)];
  end
    RK(1:5)=dec2bin(bitxor(bin2dec(RK(1:5)), i), 5);
    RK=create_state(RK, 0);
end

function res=rotl(bin, d)
  if d>1
    res=rotl([bin(2:end) bin(1)], d-1);
  else
    res=[bin(2:end) bin(1)];
  end
end

function res=rotr(bin, d)
  if d>1
    res=rotr([bin(end) bin(1:end-1)], d-1);
  else
    res=[bin(end) bin(1:end-1)];
  end
end

function res=shiftl(bin, d)
  if d>1
    res=shiftl([bin(2:end) '0'], d-1);
  else
    res=[bin(2:end) '0'];
  end
end

function res=shiftr(bin, d)
  if d>1
    res=shiftr(['0' bin(1:end-1)], d-1);
  else
    res=['0' bin(1:end-1)];
  end
end

function state=roundFnLFSM(K, d)
if d>0
  for i=1:5:16
    K(i:i+4)=[K(i+1:i+4) K(i)];
  end
end
%% L0
  state(1)=bitxor(K(1), bin2dec(rotr(dec2bin(K(5),4),1)));
  state(2)=bitxor(K(2), bin2dec(shiftr(dec2bin(K(3),4),3)));
  state(3)=K(3);
  state(4)=K(4);
  state(5)=K(5);
%% L1
  state(6)=K(6);
  state(7)=bitxor(K(7), bin2dec(shiftl(dec2bin(K(8),4),3)));
  state(8)=K(8);
  state(9)=K(9);
  state(10)=bitxor(K(10), bin2dec(rotl(dec2bin(K(9),4),1)));
%% L2
  state(11)=K(11);
  state(12)=bitxor(K(12), bin2dec(rotr(dec2bin(K(13),4),1)));
  state(13)=K(13);
  state(14)=bitxor(K(14), bin2dec(shiftr(dec2bin(K(13),4),3)));
  state(15)=K(15);
%% L3
  state(16)=K(16);
  state(17)=bitxor(K(17), bitxor(bin2dec(shiftl(dec2bin(K(16),4),3)), bin2dec(rotl(dec2bin(K(18),4),1))));
  state(18)=K(18);
  state(19)=K(19);
  state(20)=K(20);
%%%% permutaion
if (d<=0)
  for i=1:5:16
    state(i:i+4)=[state(i+4) state(i:i+3)];
  end
end
end