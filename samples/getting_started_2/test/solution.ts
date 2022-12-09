import { Peter, add } from '../solution';


describe('Samples: Getting Started 1', () => {
  describe('add', () => {
    it('human adds two numbers', () => {
      let peter: Peter = new Peter('peter', 'blue')
      expect(add(peter, 1, 2)).toBe(1 + 2);
    });
  });
});
