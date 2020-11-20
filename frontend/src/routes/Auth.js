import React from 'react';

responseKaKao = (res) => {
  const { data } = this.state;

  this.setState({
    data: res,
  });

  fetch(`${API_URL_LOGIN}/auth/signin/kakao`, {
    method: 'GET',
    headers: {
      Authorization: res.response.access_token,
    },
  })
    .then((res) => res.json())
    .then((res) => localStorage.setItem('token', res.token), alert('로그인 성공!'));
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
