%%%%
%%  LILLIPUT
%%%%
clear all

%%%%
%%  Constante
%%%%
sbox=[4 8 7 1 9 3 2 14 0 11 6 15 10 5 13 12];
perm=[13 9 14 8 10 11 12 15 4 5 3 1 2 6 0 7]; %% Encryption permutation
perm_d=[14 11 12 10 8 9 13 15 3 1 4 5 6 0 2 7]; %% Decryption permutation

source('LILLIPUT_lib.m');

%%%%
%% Example of test vectors
%%%%
MSG='0123456789abcdef';
Master_KEY='0123456789abcdef0123';
%MSG='0000000000000000';
%Master_KEY='00000000000000000000';

%%%%
%% lilliput encryption
%%%%

state_M=create_state(MSG, 1);
state_K=create_state(Master_KEY, 1);

for i=0:28
i
  RK=exctract_round_key(state_K, i, sbox);
  state_K=roundFnLFSM(state_K, 0);
  state_M=nonlinear_layer(state_M, RK, sbox);
  state_M=linear_layer(state_M);
  state_M=permutation(state_M, perm)
end
RK=exctract_round_key(state_K, 29, sbox);
state_M=linear_layer(nonlinear_layer(state_M, RK, sbox));
C='';
for i=1:16
  C=[dec2hex(state_M(i)) C];
end
C


%% 
%% lilliput decryption
%%
%

state_M=create_state(C, 1);
state_K=create_state(Master_KEY, 1);

for i=0:28
   state_K=roundFnLFSM(state_K, 0);
end
for i=29:-1:1
  i
  RK=exctract_round_key(state_K, i, sbox)
  state_K=roundFnLFSM(state_K, 1)
  state_M=nonlinear_layer(state_M, RK, sbox);
  state_M=linear_layer(state_M);
  state_M=permutation(state_M, perm_d);
end
RK=exctract_round_key(state_K, 0, sbox);
state_M=linear_layer(nonlinear_layer(state_M, RK, sbox));
MSG='';
for i=1:16
  MSG=[dec2hex(state_M(i)) MSG];
end
MSG

