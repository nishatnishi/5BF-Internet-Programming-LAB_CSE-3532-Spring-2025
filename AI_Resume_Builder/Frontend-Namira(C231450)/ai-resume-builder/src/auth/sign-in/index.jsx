import { SignIn } from "@clerk/clerk-react";
import React from "react";

function SignInPage() {
  return (
    // sing-in layout (using clerk)
    <div className="flex justify-center my-20 items-center">
      <SignIn />
    </div>
  );
}

export default SignInPage;
