import { Outlet } from "react-router-dom";

import { SiteHeader } from "./SiteHeader.jsx";

export function AppLayout() {
  return (
    <div className="layout">
      <SiteHeader />
      <main className="main main-wide">
        <Outlet />
      </main>
    </div>
  );
}
