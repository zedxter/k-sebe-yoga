Feature: Mobile hero — full-height vertical cover, text on top
  As a visitor on a mobile device
  I want the vertical hero cover shown at full natural height with the text at the top
  So that the image is not cropped and the woman is not covered by copy

  Background:
    Given the k-sebe-yoga landing page is served

  Scenario: Mobile viewport shows the whole vertical cover
    Given a viewport width of 390px
    When the page loads
    Then the rendered hero image box aspect ratio is approximately the natural ratio (1.78)
    And the hero box height is approximately viewportWidth * 1.78

  Scenario: No horizontal overflow on any mobile width
    Given viewport widths of 320, 360, 390 and 414px
    When the page layout is computed
    Then documentElement.scrollWidth - clientWidth equals 0

  Scenario: Copy block stays in the top band
    Given a mobile viewport of 390px width
    When the layout is computed
    Then the bottom edge of .hero-copy is within the top 30 percent of the hero height

  Scenario: Wide viewport keeps the desktop hero
    Given a viewport width of 1024px
    When the page renders
    Then the hero uses hero-wide.jpg (the horizontal cover)
    And the hero copy remains in the right column with left text alignment