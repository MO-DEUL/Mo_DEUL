import axios from 'axios';
import React from 'react';

responseKaKao = (res) => {
  const { data } = this.state;

  this.setState({
    data: res,
  });
};

const Auth = () => {
  return (
    <div>
      <div>
        <KaKaoBtn
          jsKey={process.env.JS_KEY}
          buttonText="카카오 계정으로 로그인"
          onSuccess={this.responseKaKao}
          getProfile={true}
        />
      </div>
    </div>
  );
};
export default Auth;
