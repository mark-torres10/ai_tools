import { render } from "@testing-library/react";
import Home from "@/app/page";

jest.mock("@/lib/api", () => ({
  fetchFeed: async () => ({ items: [], next_cursor: null }),
}));

describe("Home feed", () => {
  it("renders without crashing", async () => {
    // Home is a Client Component; render should work
    render(<Home />);
    expect(true).toBe(true);
  });
});
