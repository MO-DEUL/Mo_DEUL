import axios from 'axios';
import React from 'react';

const Auth = () => {
  return (
    <div>
      <div>
        <button
          jsKey={process.env.JS_KEY}
          buttonText="카카오 계정으로 로그인"
          onSuccess={}
          getProfile={true}
        />
      </div>
    </div>
  );
};
export default Auth;
